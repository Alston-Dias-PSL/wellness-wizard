import re
import string
import secrets
import requests
import typing
from hashlib import sha256
import datetime
import json
import os
from typing import List
import tempfile
from pydub import AudioSegment
from pyAudioAnalysis import audioSegmentation as aS
from lib.ca_config import DEFAULT_TEXT_TO_PDF_LLM , DEFAULT_TEXT_TO_TRANSCRIPT_LLM1, DEFAULT_TEXT_TO_TRANSCRIPT_LLM2, DEFAULT_TEXT_TO_AUDIO_LLM

from fastapi import FastAPI, File, UploadFile, BackgroundTasks, Form, Request, Response, HTTPException
from fastapi.responses import FileResponse, RedirectResponse, JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from pydantic import BaseModel

from Processor import Processor
from lib.DatabaseWrapper import DatabaseWrapper
from lib.SessionManagement import SessioManagement
from lib.ca_config import ip_address, DEFAULT_SERVER_PORT, DEFAULT_UI_PORT

CORS_ORIGINS = [
    "http://locahost:{}".format(DEFAULT_UI_PORT),
    "https://locahost:{}".format(DEFAULT_UI_PORT),
    "https://{}/{}".format(ip_address,DEFAULT_UI_PORT),
    "http://{}/{}".format(ip_address, DEFAULT_UI_PORT),
    "https://{}/{}".format(ip_address,DEFAULT_SERVER_PORT),
    "http://{}/{}".format(ip_address, DEFAULT_SERVER_PORT)
]

app = FastAPI()
processor = Processor()
database_wrapper = DatabaseWrapper()
session_management = SessioManagement()

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.add_middleware(GZipMiddleware)

@app.post("/create-user/")
def create_user(first_name, last_name, address_line1, city, state, country, pincode, username, password, confirm_password, email, contact_number):
    if password != confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    data = processor.get_users()
    for d in data:
        if username == d["username"]:
            raise HTTPException(status_code=409, detail="Username already exists")
    return processor.create_user(
        first_name=first_name,
        last_name=last_name,
        address_line1=address_line1,
        city=city,
        state=state,
        country=country,
        pincode=pincode,
        username=username, 
        password=password, 
        email=email, 
        contact_number=contact_number
    )

@app.get("/user-login/")
def user_login(username, password):
    user_session = processor.user_login(username=username, password=password)
    if user_session:
        session_management.update_session_info(session_data=user_session)
        return{
            "access_token": user_session["access_token"]
        } 
    else:
        raise HTTPException(status_code=404, detail="Invalid Creds")
    
@app.get("/get-user/")
def get_users(token):
    if processor.validate_jwt_token(token):
        return{
            "Validated": "Yaaahh!!! you are validated"
        }
    else:
        raise HTTPException(status_code=401, detail="Access token expired. please re-login to continue")
    
@app.post("/upload-pdf/")
async def upload_pdf(token, files: List[UploadFile] = File(...)):
    if processor.validate_jwt_token(token):
        # Assuming the user uploads a single PDF file
        uploaded_file = files[0]
    
        # Save the uploaded file temporarily
        with open(uploaded_file.filename, "wb") as file:
            file.write(uploaded_file.file.read())
    
        # Read the PDF content
        pdf_text = processor.read_pdf(file_path=uploaded_file.filename)
        pdf_text = pdf_text.replace("\n", " ")
    
        return {"filename": uploaded_file.filename, "text": pdf_text}
    else:
        raise HTTPException(status_code=401, detail="Access token expired. please re-login to continue")

@app.post("/upload-audio/")
async def upload_audio(token, audio_file: UploadFile = File(...)):
    if processor.validate_jwt_token(token):
        if not audio_file.filename.endswith((".wav", ".mp3", ".m4a")):
            raise HTTPException(status_code=400, detail="Invalid audio file format")
        audio_data = await audio_file.read()

        # Save audio data to a temporary file.
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(audio_data)
            temp_file_name = temp_file.name

        #converting the .mp3 file to text ".wav"
        if audio_file.filename.endswith((".mp3", ".m4a")):
            audio = AudioSegment.from_file(temp_file_name)
            temp_wav_file_name = temp_file_name.replace(".mp3", ".wav").replace(".m4a", ".wav")
            audio.export(temp_wav_file_name, format="wav")
            temp_file_name = temp_wav_file_name
        
        text = processor.get_text_from_audio(audio_data=temp_file_name)
        prompt_input=DEFAULT_TEXT_TO_TRANSCRIPT_LLM1 + text["text"] + DEFAULT_TEXT_TO_TRANSCRIPT_LLM2
        transcript=processor.get_transcript_from_text(text=prompt_input)
        os.remove(temp_file_name)
        transcript_new = DEFAULT_TEXT_TO_AUDIO_LLM + transcript.choices[0].message.content
        summary = processor.generate_transcript_summary(text=transcript_new)
        return {
            "transcript": transcript.choices[0].message.content, 
            "summary": summary.choices[0].message.content
        }
    
    else:
        raise HTTPException(status_code=401, detail="Access token expired. please re-login to continue")

@app.post("/generate-report-summary/")
async def generate_report_summary(token, files: List[UploadFile] = File(...)):
    if processor.validate_jwt_token(token):
        uploaded_file = files[0]
    
        # Save the uploaded file temporarily
        with open(uploaded_file.filename, "wb") as file:
            file.write(uploaded_file.file.read())
    
        # Read the PDF content
        pdf_text = processor.read_pdf(file_path=uploaded_file.filename)
        os.remove(uploaded_file.filename)
        # pdf_text = pdf_text.replace("\n", " ")
        new_pdf_text = DEFAULT_TEXT_TO_PDF_LLM + pdf_text
        response = processor.generate_report_summary(text=new_pdf_text)
        return {
            "summary": response.choices[0].message.content,
            "pdf_text": pdf_text
        }
    else:
        raise HTTPException(status_code=401, detail="Access token expired. please re-login to continue")