import os
from ibm_watsonx_ai import APIClient

wml_credentials = {
                   "url": "https://us-south.ml.cloud.ibm.com",
                   "apikey":"***********"
                  }

client = APIClient(wml_credentials)


model_id = "ibm/granite-13b-instruct-v1"


