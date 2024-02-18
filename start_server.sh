#!/bin/bash

export PYTHONPATH=$(pwd):$(pwd)/lib

# Activate python virtual environment
source venv/bin/activate

# Ensure that all the python requirements are installed
pip3 install -r requirements.txt

export HOST=0.0.0.0
export PORT=8000

# Validate all credentials before starting the server
python3 setup.py --validate

if [ $? -eq 0 ]
then
    python3 -m uvicorn ca_main:app --host ${HOST} --port ${PORT} --reload
fi