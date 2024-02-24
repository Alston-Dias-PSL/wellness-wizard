import os
from ibm_watsonx_ai import APIClient

wml_credentials = {
                   "url": "https://us-south.ml.cloud.ibm.com",
                   "apikey":"rqAIv0Uy55mNG-jW0Rn-hAHm_KOHGDSdkloGUE-Yv5Ui"
                  }

client = APIClient(wml_credentials)


model_id = "ibm/granite-13b-instruct-v1"