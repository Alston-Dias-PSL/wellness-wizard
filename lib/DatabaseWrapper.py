import requests
import datetime
import hashlib

from .ca_config import DB_CONNECTION_STRING, DB_PASSWORD, DB_USERNAME, logger

class DatabaseWrapper:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.auth = (DB_USERNAME, DB_PASSWORD)
        self.headers = {
            "Accept": "application/json",
            "Content-type": "application/json",
        }
    
    def get_id(self, database, username, additional_param = ''):
        id_text = f"{database}{username}{additional_param}"
        return f"{hashlib.md5(id_text.encode()).hexdigest()}"
    
    def intialize_view(self, database):
        return self.session.put(f"{DB_CONNECTION_STRING}/{database}/_design/default",
                                headers=self.headers,
                                json={
                                    "views":{
                                        "default":{
                                            "map": "function(doc) { emit(doc.id, doc)}"
                                        }
                                    }
                                }
                            )

    def intialize_database(self, db_name, should_partition = "false"):
        message = {
            "201": f"Successfully created database/view '{db_name}'",
            "412": f"Database/View '{db_name}' already exists",
            "409": f"Database/View for database '{db_name}' already exists"
        }

        create_db_result = self.database_create(
            database=db_name,
            partition=should_partition
        )
        if create_db_result["status_code"] in (201,412):
            logger.info(message[str(create_db_result["status_code"])])
            #create view for every database, for reading optimized data fetching
            create_view_result = self.intialize_view(
                database=db_name
            )
            if create_view_result.status_code in (201, 409):
                logger.info(message[str(create_view_result.status_code)])
            else:
                logger.error(f"failed to create view 'default' for database {db_name}")
        else:
            logger.error(f"failed to create DB '{db_name} with error {create_db_result['status_code']}'")
    
    
    def query_database(self, operation, database, partition = None, bulk = False, query={}) -> tuple:
        """
        CREATE operation: Adds a new database
        ---
        READ Operation: Fetches database information
        ---
        FIND: Search for document(s) matching supplied query
        'query' can include:
            limit (number) - Maximum number of results returned. Default is 25 [Optional]
            skip (number) - Skip the first 'n' results, where 'n' is the value specified [Optional]
            sort (json) - JSON array following sort syntax [Optional]
            fields (array) - JSON array specifying which fields of each object should be returned [Optional]
            selector (json) - includes various operators: https://docs.couchdb.org/en/3.2.2/api/database/find.html#find-selectors [Optional]
        ---
        FILTER: Filter document(s) using selector query
            'query' - Can be key-value(s) pairs that are to be included in filter results
        ---
        DELETE Operation: Removes a database
        """
        path = database + (f"/_partition/{partition}" if partition else "")
        try:
            if bulk:
                response = self.session.post(f"{DB_CONNECTION_STRING}/{database}/_bulk_docs", headers=self.headers, json={ "docs": query })
            else:
                if operation == "create":
                    response = self.session.put(f"{DB_CONNECTION_STRING}/{database}", headers=self.headers, params=query)
                if operation == "read":
                    response = self.session.get(f"{DB_CONNECTION_STRING}/{path}", headers=self.headers)
                if operation == "find":
                    response = self.session.post(f"{DB_CONNECTION_STRING}/{path}/_find", headers=self.headers, json=query)
                if operation == "filter":
                    response = self.session.post(f"{DB_CONNECTION_STRING}/{database}/_changes?filter=_selector&include_docs=true", headers=self.headers, json={ "selector": query })
                if operation == "delete":
                    response = self.session.delete(f"{DB_CONNECTION_STRING}/{database}", headers=self.headers)
            response.raise_for_status()
            return { "status_code": response.status_code, "content": response.json() }
        except requests.exceptions.RequestException as e:
            return { "status_code": e.response.status_code, "content": e.response.json() }

    def query_document(self, operation, database, partition=None, document=None, rev=None, data=None) -> tuple:
        """
        CREATE operation: Adds new document to database
        'bulk' parameter should be True for bulk inserts, with the data being a list of dicts
        ---
        READ Operation: Fetches document(s) from database
        'data' parameter requires { "include_docs": True } atleast for bulk fetches
        ---
        UPDATE Operation: Update value(s) of previously existing document
        'data' parameter must include '_rev' & '_id' fields
        ---
        DELETE Operation: Removes document(s) from database
        """
        path = database + (f"/_partition/{partition}" if partition and document and '_design/default' in document else "")
        try:
            if operation == "create":
                # Need a creation_date and modification_date for record
                data["creation_date"] = str(datetime.datetime.utcnow())
                data["modification_date"] = str(datetime.datetime.utcnow())
                response = self.session.post(f"{DB_CONNECTION_STRING}/{database}", headers=self.headers, json=data)
            if operation == "read":
                response = self.session.get(f"{DB_CONNECTION_STRING}/{path}/{document}", headers=self.headers, params=data)
            if operation == "update":
                data["modification_date"] = str(datetime.datetime.utcnow())
                response = self.session.put(f"{DB_CONNECTION_STRING}/{path}/{document}", headers=self.headers, json=data)
            if operation == "delete":
                response = self.session.delete(f"{DB_CONNECTION_STRING}/{path}/{document}?rev={rev}", headers=self.headers)
            response.raise_for_status()
            return { "status_code": response.status_code, "content": response.json() }
        except requests.exceptions.RequestException as e:
            return { "status_code": e.response.status_code, "content": e.response.json() }

    # Convenience Functions
    def database_create(self, database, partition = None) -> tuple:
        """
        CREATE operation: Adds a new database
        ---
        Args:
        'database': Name of DATABASE to be created
        partitioned: Flag whether the datbase needs partitioning or not.
        """
        return self.query_database(operation="create", database = database, query = {"partitioned": "false"})

    def database_read(self, database, partition = None) -> tuple:
        """
        READ Operation: Fetches database information
        ---
        Args:
        'database': Name of DATABASE whos information needs to be fetched
        """
        return self.query_database(operation="read", database=database, partition = partition)

    def database_delete(self, database) -> tuple:
        """
        DELETE Operation: Removes a database
        ---
        Args:
        'database': Name of DATABASE to be deleted
        """
        return self.query_database(operation="delete", database=database)

    def database_find(self, database, query, partition = None) -> tuple:
        """
        FIND: Search for document(s) matching supplied query
        ---
        Args:
        'database': Name of DATABASE to find documents from
        'query': can include-
            limit (number) - Maximum number of results returned. Default is 25 [Optional]
            skip (number) - Skip the first 'n' results, where 'n' is the value specified [Optional]
            sort (json) - JSON array following sort syntax [Optional]
            fields (array) - JSON array specifying which fields of each object should be returned [Optional]
            selector (json) - includes various operators: https://docs.couchdb.org/en/3.2.2/api/database/find.html#find-selectors [Optional]
        """
        return self.query_database(operation="find", database=database, partition = partition, query=query)

    def database_filter(self, database, query) -> tuple:
        """
        FILTER: Filter document(s) using selector query
        ---
        Args:
        'database': Name of DATABASE that the documents are to be filtered from
        'query': Can be key-value(s) pairs that are to be included in filter results
        """
        return self.query_database(operation="filter", database=database, query=query)

    def database_truncate(self, database, partition = None) -> tuple:
        """
        TRUNCATE: Remove all documents from a database except design documents
        ---
        Args:
        'database': Name of DATABASE that the documents are to be truncated from
        """
        read_result = self.document_read(database=database, partition=partition)
        if read_result["status_code"] == 200:
            data = self.get_list_from_content(read_result["content"]["rows"])
            for row in data:
                row["_deleted"] = True
            return self.query_database(operation="", database=database, partition=partition, query=data, bulk=True)
        return read_result

    def document_upsert(self, database, data, partition = None) -> tuple:
        """
        Bulk Upsert Documents: Insert or Update in Bulk
        ---
        Args:
        'database': Name of DATABASE that the documents are to be upserted into
        'data': LIST of DOCUMENTS that are to be upserted
        partition: name of the partition to insert data
        """
        return self.query_database(operation="", database=database, partition=partition, query=data, bulk=True)

    def document_create(self, database, data, partition = None) -> tuple:
        """
        CREATE operation: Adds new document to database
        Args:
        'database': Database into which the document is to be inserted
        'data': Contents of the document
        partition: name of the partition to insert data
        """
        return self.query_document(operation="create", database=database, partition=partition, data=data)

    def document_read(self, database, document="_design/default/_view/default", data="", partition = None) -> tuple:
        """
        READ Operation: Fetches document(s) from database
        ---
        Args:
        'document': DOCUMENT ID of document to be fetch. If not supplied, will return all docs in db
        'data': Extra parameters of query. Can be used to get only a set of keys out of whole doc.
                Needs { "include_docs": True } if quering for more than one doc
        """
        return self.query_document(operation="read", database=database, document=document, partition=partition, data=data)

    def document_update(self, database, document, data, partition = None) -> tuple:
        """
        UPDATE Operation: Update value(s) of previously existing document
        ---
        Args:
        'database': Database into which the document is to be updated
        'document': ID of document to be updated
        'data': Updated contents of the document. Must include '_rev' field
        """
        return self.query_document(operation="update", database=database, partition=partition, document=document, data=data)

    def document_delete(self, database, document, rev, partition = None) -> tuple:
        """
        DELETE Operation: Removes a document from database
        ---
        Args:
        'database': Database from which the document is to be deleted
        'document': ID of document to be deleted
        'rev': Must have the most recent rev(revision) value
        """
        return self.query_document(operation="delete", database=database, partition=partition, document=document, rev=rev)

    @staticmethod
    def get_list_from_content(content):
        return list(map(lambda doc: doc["doc"] if "doc" in doc else doc["value"], content))    