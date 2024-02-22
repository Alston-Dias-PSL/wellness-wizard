import re
import string
import secrets
import requests
import typing
from hashlib import sha256
import datetime
import json

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
    


   