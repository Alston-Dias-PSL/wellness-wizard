from lib.UserInfo import UserInfoProcessor
from lib.DatabaseWrapper import DatabaseWrapper

class Processor:
    def __init__(self):
        self.user_info =  UserInfoProcessor()
        self.databse_wrapper = DatabaseWrapper()

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
