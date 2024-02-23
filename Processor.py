from lib.UserInfo import UserInfoProcessor
from lib.DatabaseWrapper import DatabaseWrapper
from lib.JWTProcessor import JWTProcessor

class Processor:
    def __init__(self):
        self.user_info =  UserInfoProcessor()
        self.databse_wrapper = DatabaseWrapper()
        self.jwt_processor = JWTProcessor()

    def create_user(self,first_name, last_name, address_line1, city, state, country, pincode, username, password,  email, contact_number):
        return self.user_info.create_user(
            first_name=first_name,
            last_name=last_name,
            address_line1=address_line1,
            city=city,
            state=state,
            country=country,
            pincode=pincode,
            username=username,
            password=password, 
            email=email, 
            contact_number=contact_number
        )
    
    def get_users(self):
        return self.user_info.get_users()
    
    def verify_password(self, plain_password, encrypted_password):
        return self.user_info.verify_password(plain_password, encrypted_password)
    
    def get_user_by_username(self, username):
        return self.user_info.get_user_by_username(username=username)
    
    def user_login(self, username, password):
        return self.jwt_processor.login_for_access_token(username, password)
    
    def validate_jwt_token(self, token):
        return self.jwt_processor.validate_jwt_token(token=token)
    
