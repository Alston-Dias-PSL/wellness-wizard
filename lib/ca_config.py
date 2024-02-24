import json
from pathlib import Path
import os
import socket
import logging

# Intialize logging config
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    ip_address = socket.gethostbyname('host.docker.internal')
except:
    ip_address = socket.gethostbyname(socket.gethostname())

#General Configuration
HOME = str(Path(__file__).resolve().parent.parent)
DEFAULT_UI_PORT = "3000"
DEFAULT_SERVER_PORT = "8000"

#getting data from .credentials.json
try:
    with open("{}/.credentials.json".format(HOME)) as json_file:
        json_data = json.load(json_file)
except FileNotFoundError as fne:
    json_data = {
        "DB_CONNECTION_STRING": os.environ.get("db_connection_string", "http://localhost:5984"),
        "DB_USERNAME": os.environ.get("db_username", "semicolons"),
        "DB_PASSWORD": os.environ.get("db_password", "alstondias"),
        "JWT_SECRET_KEY": os.environ.get("jwt_secret_key", ""),
        "SEMICOLONS_GATEWAY_API_KEY": os.environ.get("semicolons_gateway_api_key", ""),
        "SEMICOLONS_GATEWAY_BASE_URL": os.environ.get("semicolons_gateway_base_url", ""),
    }
# Required Databased
REQUIRED_DBS = {
    "user_info": "false",
    "user_session": "false"
}

# Databse configurations
DB_CONNECTION_STRING = json_data["DB_CONNECTION_STRING"]
DB_USERNAME = json_data["DB_USERNAME"]
DB_PASSWORD = json_data["DB_PASSWORD"]

#JWT configuration
JWT_SECRET_KEY = json_data["JWT_SECRET_KEY"]
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES_IN = 24

#LLM configuration
SEMICOLONS_GATEWAY_API_KEY = json_data["SEMICOLONS_GATEWAY_API_KEY"]
SEMICOLONS_GATEWAY_BASE_URL = json_data["SEMICOLONS_GATEWAY_BASE_URL"]
MODEL = "gpt-35-turbo-16k"
AUDIO_MODEL = "gpt-4-turbo"
DEFAULT_TEXT_TO_PDF_LLM = """ Give me a summarized report for the following blood report and also give potential risks for the patient 
"""
DEFAULT_TEXT_TO_AUDIO_LLM = """Give me a summarized report for the following text conversation between a doctor and patient"""

DEFAULT_TEXT_TO_TRANSCRIPT_LLM1 = """Generate a transcript for the following text conversation between a doctor and patient
Text:
"""
DEFAULT_TEXT_TO_TRANSCRIPT_LLM2 = """Give the Transcript in the format :
Doctor: Dialogue1
Patient:Dialogue2
Doctor:Dialogue3"""
