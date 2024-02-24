import speech_recognition as sr
from pydub import AudioSegment

class AudioProessor:

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

