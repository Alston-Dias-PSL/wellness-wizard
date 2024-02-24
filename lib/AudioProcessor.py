from openai import OpenAI
import speech_recognition as sr
from .ca_config import SEMICOLONS_GATEWAY_API_KEY, SEMICOLONS_GATEWAY_BASE_URL, AUDIO_MODEL,MODEL

class AudioProessor:

    client = OpenAI(
            api_key=SEMICOLONS_GATEWAY_API_KEY,
            base_url=SEMICOLONS_GATEWAY_BASE_URL,
            # base_url represents the endpoint the OpenAI object will make a call to when invoked
        )
    
    def get_text_from_audio(self, audio_data):
        recognizer = sr.Recognizer()
        try:
            with sr.AudioFile(audio_data) as source:
                audio = recognizer.record(source)
                text = recognizer.recognize_google(audio)
                return {"text": text}
        except sr.UnknownValueError:
            return {"error": "Could not understand audio"}
        except sr.RequestError as e:
            return {"error": f"Could not request result {e}"}
    
    def get_transcript_from_text(self,text):
        prompt_input = text
        print("Submitting generation request...")
        generated_response = self.client.chat.completions.create(model=AUDIO_MODEL,  temperature=0.1, messages=[{"role": "user", "content": prompt_input},])
        return generated_response
    
    def generate_transcript_summary(self, text):
      prompt_input = text
      print("Submitting generation request...")
      generated_response = self.client.chat.completions.create(model=MODEL,  temperature=0.1, messages=[{"role": "user", "content": prompt_input},])
      return generated_response

                        
