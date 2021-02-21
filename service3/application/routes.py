from flask import request, Response
import requests
from application import app
import random

#generates second zodiac sign

@app.route('/second_sign', methods = ['GET'])
def second_sign():
    signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
    sign = signs[random.randrange(0,12)]
    return Response(sign, mimetype = "text/plain")



