from openai import OpenAI
from .ca_config import SEMICOLONS_GATEWAY_API_KEY, SEMICOLONS_GATEWAY_BASE_URL, MODEL

class LLMProcessor:

  client = OpenAI(
      api_key=SEMICOLONS_GATEWAY_API_KEY,
      base_url=SEMICOLONS_GATEWAY_BASE_URL,
      # base_url represents the endpoint the OpenAI object will make a call to when invoked
  )

  def generate_report_summary(self, text):
      prompt_input = text
      print("Submitting generation request...")
      generated_response = self.client.chat.completions.create(model=MODEL,  temperature=0.1, messages=[{"role": "user", "content": prompt_input},])
      return generated_response