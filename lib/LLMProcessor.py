import ca_main
from Processor import Processor
model = "gpt-35-turbo-16k"
# model = "amazon.titan-text-lite-v1"

### Enter your Credentials
semicolons_gateway_api_key = "sk-aqJlo8WijMhjQsripvbzhw" # Insert the provided API key
semicolons_gateway_base_url = "https://4veynppxjm.us-east-1.awsapprunner.com"


from openai import OpenAI

client = OpenAI(
    api_key=semicolons_gateway_api_key,
    base_url=semicolons_gateway_base_url,
    # base_url represents the endpoint the OpenAI object will make a call to when invoked
)

def generate_report_summary(self, text):
    prompt_input = text
    print("Submitting generation request...")
    generated_response = client.chat.completions.create(model=model,  temperature=0.1, messages=[{"role": "user", "content": prompt_input},])
    return generated_response


# print(response.model_dump()["choices"][0]["message"]["content"])



























# import os
# #from ibm_watsonx_ai import APIClient
# from ibm_watson_machine_learning.foundation_models import Model

# from .ca_config import SPACE_ID, PROJECT_ID, WATSONX_API_KEY, WATSONX_URL

# class LLMProcessor:

#   wml_credentials = {
#                     "url": WATSONX_URL,
#                     "apikey": WATSONX_API_KEY,
#                     }

#   model_id = "google/flan-ul2"

#   parameters = {
#       "decoding_method": "sample",
#       "max_new_tokens": 300,
#       "temperature": 0.6,
#       "top_k": 72,
#       "top_p": 1,
#       "repetition_penalty": 2
#   }

#   model = Model(
#     model_id = model_id,
#     params = parameters,
#     credentials = wml_credentials,
#     project_id = PROJECT_ID,
#     space_id = SPACE_ID
#   )

#   def generate_report_summary(self, text):
#     prompt_input = text
#     print("Submitting generation request...")
#     generated_response = self.model.generate_text(prompt=prompt_input, guardrails=False)
#     return generated_response

### Model to be Invoked

