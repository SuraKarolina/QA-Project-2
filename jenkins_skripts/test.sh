#!/bin/bash

# test servcie1
cd ./service1
pip3 install -r requirements.txt
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml 
cd ..

# test servcie2
cd ./service2
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
cd ..

# test servcie3
cd ./service3
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
cd ..

# test servcie4
cd ./service4
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
cd ..