import json
from pathlib import Path
import os
import logging

# Intialize logging config
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

#General Configuration
HOME = str(Path(__file__).resolve().parent.parent)

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