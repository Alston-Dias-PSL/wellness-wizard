import json
import os
import requests
import random
import string

from fastapi import HTTPException

from .ca_config import *
from .DatabaseWrapper import DatabaseWrapper
from passlib.context import CryptContext
from .SessionManagement import SessioManagement

class UserInfoProcessor:
    database_wrappeer = DatabaseWrapper()
    session_management = SessioManagement()
    user_collection_name = "user_info"
    pwd_contxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def store_data_to_db(self, user_data, collection_name = None):
        if not collection_name:
            collection_name = self.user_collection_name
        create_result = self.database_wrappeer.database_create(collection_name)
        if create_result["status_code"] == 412:
            print("Database aleady exists: ", collection_name)
        return self.database_wrappeer.document_create(
            collection_name,
            user_data,
        )
    
    def genrate_wellness_number():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    
    def create_user(self,first_name, last_name, address_line1, city, state, country, pincode,  username, password,  email, contact_number):
        password = self.pwd_contxt.hash(password)
        # wellness_number = self.genrate_wellness_number()
        user_data ={
            "first_name": first_name,
            "last_name": last_name,
            "address_line1": address_line1,
            "city": city,
            "state": state,
            "country": country,
            "pincode": pincode,
            "username": username,
            "password": password,
            "email": email,
            "contact_number": contact_number,
            # "wellness_number": wellness_number
        }
        return self.store_data_to_db(user_data=user_data)
    
    def get_users(self):
        data = self.database_wrappeer.document_read(
            self.user_collection_name
        )
        if data["status_code"] < 400:
            return self.database_wrappeer.get_list_from_content(data["content"]["rows"])
    
    def get_user_by_username(self, username):
        data = self.get_users()
        for user in data:
            if username == user["username"]:
                return user
    
    def verify_password(self, plain_passeword, hashed_password):
        return self.pwd_contxt.verify(plain_passeword, hashed_password)
    
    def user_login(self, username, password):
        user = self.get_user_by_username(username=username)
        if user:
            passwd = self.verify_password(password, user["password"])
            if passwd:
                return user
            else:
                raise HTTPException(status_code=400, detail="username or password do not match")
        else:
            raise HTTPException(status_code=404, detail=f"user with {username} not found")
        
    
