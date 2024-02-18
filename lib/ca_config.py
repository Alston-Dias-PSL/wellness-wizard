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
        "db_connection_string": os.environ.get("db_connection_string", "http://localhost:5984"),
        "db_username": os.environ.get("db_username", "semicolons"),
        "db_password": os.environ.get("db_password", "alstondias")
    }
# Databse configurations
DB_CONNECTION_STRING = json_data["DB_CONNECTION_STRING"]
DB_USERNAME = json_data["DB_USERNAME"]
DB_PASSWORD = json_data["DB_PASSWORD"]