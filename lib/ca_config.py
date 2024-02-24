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
DEFAULT_TEXT_TO_PDF_LLM = """Given the following medical reports as input, use it to generate a summary according to the output given to you. It should have simple, easy-to-understand language so that a patient can understand it easily. 

Medical Report Complete Blood Count (CBC):
White Blood Cell Count (WBC): 7,500 cells/mcL (Normal Range: 4,000 - 11,000 cells/mcL)
Red Blood Cell Count (RBC): 4.2 million cells/mcL (Normal Range: 4.5 - 5.5 million cells/mcL)
Hemoglobin (Hb): 12.8 g/dL (Normal Range: 12.0 - 15.0 g/dL)
Hematocrit (Hct): 38% (Normal Range: 38.3 - 48.6%)
Platelet Count: 80,000 platelets/mcL (Normal Range: 150,000 - 450,000 platelets/mcL)
Peripheral Blood Smear:
Microcytic and hypochromic red blood cells
Mean Corpuscular Volume (MCV): 80 fL (Normal Range: 80 - 100 fL)
Mean Corpuscular Hemoglobin (MCH): 28 pg (Normal Range: 27 - 33 pg)
Decreased platelet count with few giant platelets
Coagulation Profile:
Bleeding Time: 8 minutes (Normal Range: 1 - 9 minutes)
Prothrombin Time (PT): Within normal range
Activated Partial Thromboplastin Time (aPTT): Within normal range
Additional Findings:
Iron studies show low serum iron and ferritin levels.
Vitamin B12 and folate levels are within normal range.
Summarised report Sarah Miller's detailed blood report indicates thrombocytopenia, with a platelet count of 80,000 platelets/mcL. The peripheral blood smear reveals microcytic and hypochromic red blood cells and a decreased platelet count with giant platelets. Coagulation profile shows a prolonged bleeding time. Iron studies suggest a potential iron deficiency anemia contributing to thrombocytopenia. Further consultation with a hematologist is advised for a thorough diagnosis and to determine the appropriate treatment plan, possibly involving the management of iron deficiency alongside addressing the platelet-related concerns.

Medical Report Patient: John Doe
Complete Blood Count (CBC):
White Blood Cell Count (WBC): 3,200 cells/mcL (Normal Range: 4,000 - 11,000 cells/mcL)
Red Blood Cell Count (RBC): 4.5 million cells/mcL (Normal Range: 4.5 - 5.5 million cells/mcL)
Hemoglobin (Hb): 13.5 g/dL (Normal Range: 13.8 - 17.2 g/dL)
Hematocrit (Hct): 40% (Normal Range: 38.3 - 48.6%)
Platelet Count: 200,000 platelets/mcL (Normal Range: 150,000 - 450,000 platelets/mcL)
Differential White Blood Cell Count:
Neutrophils: 40% (Normal Range: 50-70%)
Absolute Neutrophil Count: 1,280 cells/mcL
Lymphocytes: 45% (Normal Range: 20-40%)
Absolute Lymphocyte Count: 1,440 cells/mcL
Monocytes: 10% (Normal Range: 2-10%)
Absolute Monocyte Count: 320 cells/mcL
Eosinophils: 3% (Normal Range: 1-6%)
Absolute Eosinophil Count: 96 cells/mcL
Basophils: 2% (Normal Range: 0-2%)
Absolute Basophil Count: 64 cells/mcL
Summarised report Leukopenia is evident, with a decreased white blood cell count. The specific differential count indicates a relative decrease in neutrophils and lymphocytes. Further investigation, including additional blood tests and consultation with a haematologist, is recommended to identify the underlying cause and determine appropriate management.

Medical Report Patient: James Anderson
Complete Blood Count (CBC):
- White Blood Cell Count (WBC): 7,800 cells/mcL (Normal Range: 4,000 - 11,000 cells/mcL)
- Red Blood Cell Count (RBC): 4.0 million cells/mcL (Normal Range: 4.5 - 5.5 million cells/mcL)
- Hemoglobin (Hb): 11.5 g/dL (Normal Range: 12.0 - 15.0 g/dL)
- Hematocrit (Hct): 35% (Normal Range: 38.3 - 48.6%)
- Platelet Count: 25,000 platelets/mcL (Normal Range: 150,000 - 450,000 platelets/mcL)
Peripheral Blood Smear:
- Microcytic and hypochromic red blood cells
  - Mean Corpuscular Volume (MCV): 75 fL (Normal Range: 80 - 100 fL)
  - Mean Corpuscular Hemoglobin (MCH): 28 pg (Normal Range: 27 - 33 pg)
- Severe thrombocytopenia with fragmented red blood cells (schistocytes)
- Presence of helmet cells
Coagulation Profile:
- Bleeding Time: 10 minutes (Normal Range: 1 - 9 minutes)
- Prothrombin Time (PT): Within normal range
- Activated Partial Thromboplastin Time (aPTT): Within normal range
Additional Findings:
- Elevated lactate dehydrogenase (LDH) levels: 800 U/L (Normal Range: 135 - 214 U/L)
- Decreased haptoglobin levels: 10 mg/dL (Normal Range: 30 - 200 mg/dL)

Summarised report"""