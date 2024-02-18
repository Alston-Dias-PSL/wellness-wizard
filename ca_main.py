import re
import string
import secrets
import requests
import typing
from hashlib import sha256
import datetime
import json

from fastapi import FastAPI, File, UploadFile, BackgroundTasks, Form, Request, Response
from fastapi.response import FileResponse, RedirectResponse, JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from pydantic import BaseModel
from apscheduler.schedulers.background import BackgroundScheduler

from lib.DatabaseWrapper import DatabaseWrapper
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
