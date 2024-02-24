import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('z2morIDKm5vik-_TjYYc8RcMW5NrPrtUnqX2WFt74Iun')
assistant = AssistantV2(
    version='2021-06-14',
    authenticator = authenticator
)

assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com/instances/b9c7c642-a9d1-4526-acea-4f39d9aeec41')

environment_id="aab9c6f5-88eb-4c94-ac1b-5928945f5134"

session = assistant.create_session(environment_id).get_result()


def send_message(message):
    response = assistant.message(
        assistant_id=environment_id,
        session_id=session["session_id"],
        input={
            'message_type': 'text', 
            'text': message,
        }
    ).get_result()


    return response["output"]["generic"][0]["text"]


user_input = input("Hello, How can I help you today?")
while user_input.lower() != "thank you":
    response = send_message(user_input)
    print("WatsonX Assistant: ", response)
    user_input = input("Enter your message:")

# print(json.dumps(response, indent=2))