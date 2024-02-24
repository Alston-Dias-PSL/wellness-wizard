import requests

url = "https://us-south.ml.cloud.ibm.com/ml/v1-beta/generation/text?version=2023-05-29"

body = {
	"input": """prompt_input = \"\"\"Act as a doctor'\''s assistant and examine the given scenario provided in the description and categorise the disease. 


Description:   - Disruption of food supplies and inadequate access to nutritious food can contribute to malnutrition, especially among vulnerable populations.
Name: Malnutrition 


Description:  - Trauma, stress, and loss experienced during natural disasters can lead to mental health challenges, including anxiety, depression, and post-traumatic stress disorder (PTSD).
Name: Mental Health Issues


Description:   - Physical injuries during a disaster can result in wounds susceptible to infections if not properly treated and managed.
Name: Injuries and Wound Infections


Description:   - Poor sanitation, crowded shelters, and exposure to dust or mold can lead to respiratory infections, including influenza and pneumonia.
Name: Respiratory Infections

The following paragraph is a dialogue between doctor and patient. The scenario must be classified in one of the categories described above. Read the following description and determine which category the scenario is about. Make sure to use exactly one of the names of the categories listed above. 

The patient reports coughing, shortness of breath, and chest discomfort with a low-grade fever. The doctor recommends diagnostic tests, prescribes medication, and advises rest and fluids. Follow-up appointments are emphasized to monitor and adjust the treatment plan as necessary.

Name of the category:""",
	"parameters": {
		"decoding_method": "greedy",
		"max_new_tokens": 20,
		"repetition_penalty": 1
	},
	"model_id": "google/flan-ul2",
	"project_id": "0a65edce-918f-4507-921b-2d837b22627a"
}

headers = {
	"Accept": "application/json",
	"Content-Type": "application/json",
	"Authorization": "Bearer rqAIv0Uy55mNG-jW0Rn-hAHm_KOHGDSdkloGUE-Yv5Ui"
}

response = requests.post(
	url,
	headers=headers,
	json=body
)

if response.status_code != 200:
	raise Exception("Non-200 response: " + str(response.text))

data = response.json()