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
        "WATSONX_API_KEY": os.environ.get("watsonx_api_key", ""),
        "WATSONX_URL": os.environ.get("watsonx_url", ""),
        "PROJECT_ID": os.environ.get("project_id", ""),
        "SPACE_ID": os.environ.get("space_id", "")
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
PROJECT_ID = json_data["PROJECT_ID"]
SPACE_ID = json_data["SPACE_ID"]
WATSONX_API_KEY = json_data["WATSONX_API_KEY"]
WATSONX_URL = json_data["WATSONX_URL"]
DEFAULT_TEXT_TO_PDF_LLM = """ Give me a summarized report for the following blood report and also give potential risks for the patient 
"""