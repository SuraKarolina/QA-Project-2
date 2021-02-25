from flask import request,Response
import requests
from application import app
import random

# generates first zodiac sign
@app.route('/first_sign', methods = ['GET'])
def first_sign():
    signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
    sign = signs[random.randrange(0,12)]
    return Response(str(sign), mimetype="text/plain")



