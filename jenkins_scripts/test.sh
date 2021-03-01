#!/bin/bash
pwd
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
cd service1
python3 -m pytest --cov application
python3 -m pytest --cov application
cd ../service2
python3 -m pytest --cov application
cd ../service3
python3 -m pytest --cov application
cd ../service4
python3 -m pytest --cov application
cd ..
deactivate