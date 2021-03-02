from flask import render_template, url_for, Response, request, jsonify
from application import app, db
from application.models import Match
import requests
import json


@app.route('/')
@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route('/home', methods = ['GET', 'POST'])
def home():
    #get first zodiac sign
    first_sign = requests.get("http://localhost:5001/first_sign")

    #get second zodiac sign
    second_sign = requests.get("http://localhost:5002/second_sign")

    #get description
    description = requests.get("http://localhost:5003/description", json = {"first_sign" : first_sign.text, "second_sign" : second_sign.text})

    new_match = {"first_sign" : first_sign.text, "second_sign" : second_sign.text}

    return render_template('home.html', first_sign = first_sign.text, second_sign = second_sign.text, description = description.text, new_match = new_match)

