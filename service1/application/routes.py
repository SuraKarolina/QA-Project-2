from flask import render_template, url_for, Response, request
from application import app, db
from application.models import Match
import requests
import random


@app.route('/')
@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route('/home', methods = ['GET'])
def home():
    #get first zodiac sign
    first_sign = requests.get("http://localhost:5001/first_sign")

    #get second zodiac sign
    second_sign = requests.get("http://localhost:5002/second_sign")

    #get description
    description = requests.get("http://localhost:5003/description", data = first_sign and second_sign)

    return render_template('home.html', first_sign = first_sign, second_sign = second_sign, description = description)

