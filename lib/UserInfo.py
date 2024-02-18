import json
import os
import requests

from ca_config import *
from .DatabaseWrapper import DatabaseWrapper

class UserInfoProcessor:
    database_wrappeer = DatabaseWrapper()
    user_collection_name = "user_info"

    def store_data_to_db(self, user_data, collection_name = None):
        if not collection_name:
            collection_name = self.user_collection_name
        create_result = self.database_wrappeer.database_create(collection_name)
        if create_result["status_code"] == 412:
            print("Database aleady exists: ", collection_name)
        return self.database_wrappeer.document_upsert(
            collection_name,
            user_data,
        )