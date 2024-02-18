import json
import requests
from lib.ca_config import REQUIRED_DBS
from multiprocessing import Process
import uvicorn
import argparse
from os.path import exists

def get_db():
    while True:
        DB_CONNECTION_STRING = input("Enter Database connection string: ")
        DB_USERNAME =  input("Enter Database Username: ")
        DB_PASSWORD = input("Enter Database Password: ")
        if validate_db(DB_CONNECTION_STRING, DB_USERNAME, DB_PASSWORD):
            return DB_CONNECTION_STRING, DB_USERNAME, DB_PASSWORD

def validate_db(DB_CONNECTION_STRING, DB_USERNAME, DB_PASSWORD):
    print("====== Testing Database ======")
    try:
        response = requests.get(DB_CONNECTION_STRING + "/_all_dbs", auth=(DB_USERNAME, DB_PASSWORD))
        if response.status_code == 200:
            print("Database connetion tested successfully!")
            return True
        response.raise_for_status()
    except:
        print("Database connection test failed. Please check string/server...")
        return False
    
def intialise_database():
    from lib.DatabaseWrapper import DatabaseWrapper
    database_wrapper = DatabaseWrapper()
    for i in REQUIRED_DBS:
        database_wrapper.intialize_database(i, "false")

def get_credentials():
    DB_CONNECTION_STRING, DB_USERNAME, DB_PASSWORD = get_db()
    json_data = {
        "DB_CONNECTION_STRING": DB_CONNECTION_STRING,
        "DB_USERNAME": DB_USERNAME,
        "DB_PASSWORD": DB_PASSWORD,
    }
    return json_data

class Uvicorn:
    proc = None
    def run(self):
        uvicorn.run("ca_main:app", host="0.0.0.0", port=8000, log_level="critical")
    
    def start(self):
        self.proc = Process(target=self.run, args=(), daemon=True)
        self.proc.start()
    
    def stop(self):
        if self.proc:
            self.proc.join(0.25)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--validate", help="Only perform validation", action="store_true")
    args = parser.parse_args()
    print(args)

    if args.validate:
        try: 
            with open(".credentials.json", "r") as json_file:
                json_data = json.load(json_file)
                if validate_db(json_data["DB_CONNECTION_STRING"], json_data["DB_USERNAME"], json_data["DB_PASSWORD"]):
                    intialise_database()
                    print('Creating databases')
                    exit(0)
                else:
                    exit(1)
        except FileNotFoundError:
            print(".credentials.json does not exist!")
            exit(2)

    # Create new credentials
    if not exists(".credentials.json"):
        print(".credentials.json file not found .\n")
        with open(".credentials.json", "w") as json_file:
            json.dump(get_credentials(), json_file)