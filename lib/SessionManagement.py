from .ca_config import *
from .DatabaseWrapper import DatabaseWrapper

class SessioManagement:
    database_wrapper =  DatabaseWrapper()
    collection_name = "user_session"

    def __init__(self):
        try:
            self.database_wrapper.database_create(self.collection_name)
        except Exception as ex:
            print("Database already exists")
    
    def get_user_session(self, username):
        data = self.database_wrapper.document_read(
            self.collection_name
        )
        data = data["content"]["rows"]
        if data:
            for session in data:
                session = session["value"]
                if username == session["username"]:
                    return session
        else:
            return None
    def remove_session(self, session_key, rev):
        try:
            return self.database_wrapper.document_delete(self.collection_name, session_key, rev)
        except (KeyError, IndexError) as ke:
            raise KeyError("Requested session does not exists")
        
    def update_session_info(self, session_data):
        session = self.get_user_session(session_data["username"])
        if session:
           self.database_wrapper.document_delete(document=session["_id"], rev=session["_rev"], database=self.collection_name, partition=None)
        
        return self.database_wrapper.document_create(
            self.collection_name,
            session_data
        )   