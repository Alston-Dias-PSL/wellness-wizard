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

# response = assistant.message(
#     assistant_id=environment_id,
#     session_id=session["session_id"],
#     input={
#         'message_type': 'text', 
#         'text': 'Book'
#     }
# ).get_result()



response=assistant.message(
    assistant_id=environment_id,
    session_id=session["session_id"],
    input={
        'message_type': 'text',
        'text': 'Hi',
        'options': {
            'return_context': True
        }
    },
    context={
        'global': {
            'system': {
                'user_id': '16b77c1a1f7d45cd89aeed8a6212d604'
            }
        },
        'skills': {
            'main skill': {
                'user_defined': {
                    'account_number': '2754586'
                }
            }
        }
    }
).get_result()


print(response["output"]["generic"][0]["text"])

# print(json.dumps(response, indent=2))