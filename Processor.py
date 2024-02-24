from lib.UserInfo import UserInfoProcessor
from lib.DatabaseWrapper import DatabaseWrapper
from lib.JWTProcessor import JWTProcessor
from lib.PdfProcessor import PdfProcessor
from lib.AudioProcessor import AudioProessor
from lib.LLMProcessor import LLMProcessor

class Processor:
    def __init__(self):
        self.user_info =  UserInfoProcessor()
        self.databse_wrapper = DatabaseWrapper()
        self.jwt_processor = JWTProcessor()
        self.pdf_processor = PdfProcessor()
        self.audio_processor = AudioProessor()
        self.llm_processor = LLMProcessor()

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
    
    def read_pdf(self, file_path: str):
        return self.pdf_processor.read_pdf(file_path=file_path)
    
    def get_text_from_audio(self, audio_data):
        return self.audio_processor.get_text_from_audio(audio_data=audio_data)
    
    def generate_report_summary(self, text):
        return self.llm_processor.generate_report_summary(text=text)
    
