import unittest
from flask import url_for
from flask_testing import TestCase
from os import getenv
import requests_mock

from application import app

class Testbase(TestCase):
    def create_app(self):
        return app

class TestCreate(Testbase):

#Aries
    def test_Aries1(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aries", "second_sign":"Aries"})
        self.assertIn(response.data, [b'50%'])
    def test_Aries2(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aries", "second_sign":"Taurus"})
        self.assertIn(response.data, [b'38%'])
    def test_Aries3(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aries", "second_sign":"Gemini"})
        self.assertIn(response.data, [b'83%'])
    def test_Aries4(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aries", "second_sign":"Cancer"})
        self.assertIn(response.data, [b'42%'])
    def test_Aries5(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aries", "second_sign":"Leo"})
        self.assertIn(response.data, [b'97%'])
    def test_Aries6(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aries", "second_sign":"Virgo"})
        self.assertIn(response.data, [b'63%'])
    def test_Aries7(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aries", "second_sign":"Libra"})
        self.assertIn(response.data, [b'85%'])
    def test_Aries8(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aries", "second_sign":"Scorpio"})
        self.assertIn(response.data, [b'50%'])
    def test_Aries9(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aries", "second_sign":"Sagittarius"})
        self.assertIn(response.data, [b'93%'])
    def test_Aries10(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aries", "second_sign":"Capricorn"})
        self.assertIn(response.data, [b'47%'])
    def test_Aries11(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aries", "second_sign":"Aquarius"})
        self.assertIn(response.data, [b'78%'])
    def test_Aries12(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aries", "second_sign":"Pisces"})
        self.assertIn(response.data, [b'67%'])


#Taurus
    def test_Taurus1(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Taurus", "second_sign":"Aries"})
        self.assertIn(response.data, [b'38%'])
    def test_Taurus2(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Taurus", "second_sign":"Taurus"})
        self.assertIn(response.data, [b'65%'])
    def test_Taurus3(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Taurus", "second_sign":"Gemini"})
        self.assertIn(response.data, [b'33%'])
    def test_Taurus4(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Taurus", "second_sign":"Cancer"})
        self.assertIn(response.data, [b'97%'])
    def test_Taurus5(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Taurus", "second_sign":"Leo"})
        self.assertIn(response.data, [b'73%'])
    def test_Taurus6(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Taurus", "second_sign":"Virgo"})
        self.assertIn(response.data, [b'90%'])
    def test_Taurus7(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Taurus", "second_sign":"Libra"})
        self.assertIn(response.data, [b'65%'])
    def test_Taurus8(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Taurus", "second_sign":"Scorpio"})
        self.assertIn(response.data, [b'88%'])
    def test_Taurus9(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Taurus", "second_sign":"Sagittarius"})
        self.assertIn(response.data, [b'30%'])
    def test_Taurus10(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Taurus", "second_sign":"Capricorn"})
        self.assertIn(response.data, [b'98%'])
    def test_Taurus11(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Taurus", "second_sign":"Aquarius"})
        self.assertIn(response.data, [b'58%'])
    def test_Taurus12(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Taurus", "second_sign":"Pisces"})
        self.assertIn(response.data, [b'85%'])

#Gemini
    def test_Gemini1(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Gemini", "second_sign":"Aries"})
        self.assertIn(response.data, [b'83%'])
    def test_Gemini2(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Gemini", "second_sign":"Taurus"})
        self.assertIn(response.data, [b'33%'])
    def test_Gemini3(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Gemini", "second_sign":"Gemini"})
        self.assertIn(response.data, [b'60%'])
    def test_Gemini4(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Gemini", "second_sign":"Cancer"})
        self.assertIn(response.data, [b'65%'])
    def test_Gemini5(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Gemini", "second_sign":"Leo"})
        self.assertIn(response.data, [b'88%'])
    def test_Gemini6(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Gemini", "second_sign":"Virgo"})
        self.assertIn(response.data, [b'68%'])
    def test_Gemini7(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Gemini", "second_sign":"Libra"})
        self.assertIn(response.data, [b'93%'])
    def test_Gemini8(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Gemini", "second_sign":"Scorpio"})
        self.assertIn(response.data, [b'28%'])
    def test_Gemini9(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Gemini", "second_sign":"Sagittarius"})
        self.assertIn(response.data, [b'60%'])
    def test_Gemini10(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Gemini", "second_sign":"Capricorn"})
        self.assertIn(response.data, [b'68%'])
    def test_Gemini11(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Gemini", "second_sign":"Aquarius"})
        self.assertIn(response.data, [b'85%'])
    def test_Gemini12(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Gemini", "second_sign":"Pisces"})
        self.assertIn(response.data, [b'53%'])


#Cancer
    def test_Cancer1(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Cancer", "second_sign":"Aries"})
        self.assertIn(response.data, [b'42%'])
    def test_Cancer2(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Cancer", "second_sign":"Taurus"})
        self.assertIn(response.data, [b'97%'])
    def test_Cancer3(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Cancer", "second_sign":"Gemini"})
        self.assertIn(response.data, [b'65%'])
    def test_Cancer4(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Cancer", "second_sign":"Cancer"})
        self.assertIn(response.data, [b'75%'])
    def test_Cancer5(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Cancer", "second_sign":"Leo"})
        self.assertIn(response.data, [b'35%'])
    def test_Cancer6(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Cancer", "second_sign":"Virgo"})
        self.assertIn(response.data, [b'90%'])
    def test_Cancer7(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Cancer", "second_sign":"Libra"})
        self.assertIn(response.data, [b'43%'])
    def test_Cancer8(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Cancer", "second_sign":"Scorpio"})
        self.assertIn(response.data, [b'94%'])
    def test_Cancer9(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Cancer", "second_sign":"Sagittarius"})
        self.assertIn(response.data, [b'53%'])
    def test_Cancer10(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Cancer", "second_sign":"Capricorn"})
        self.assertIn(response.data, [b'83%'])
    def test_Cancer11(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Cancer", "second_sign":"Aquarius"})
        self.assertIn(response.data, [b'27%'])
    def test_Cancer12(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Cancer", "second_sign":"Pisces"})
        self.assertIn(response.data, [b'98%'])

#Leo
    def test_Leo1(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Leo", "second_sign":"Aries"})
        self.assertIn(response.data, [b'97%'])
    def test_Leo2(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Leo", "second_sign":"Taurus"})
        self.assertIn(response.data, [b'73%'])
    def test_Leo3(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Leo", "second_sign":"Gemini"})
        self.assertIn(response.data, [b'88%'])
    def test_Leo4(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Leo", "second_sign":"Cancer"})
        self.assertIn(response.data, [b'35%'])
    def test_Leo5(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Leo", "second_sign":"Leo"})
        self.assertIn(response.data, [b'45%'])
    def test_Leo6(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Leo", "second_sign":"Virgo"})
        self.assertIn(response.data, [b'35%'])
    def test_Leo7(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Leo", "second_sign":"Libra"})
        self.assertIn(response.data, [b'97%'])
    def test_Leo8(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Leo", "second_sign":"Scorpio"})
        self.assertIn(response.data, [b'58%'])
    def test_Leo9(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Leo", "second_sign":"Sagittarius"})
        self.assertIn(response.data, [b'93%'])
    def test_Leo10(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Leo", "second_sign":"Capricorn"})
        self.assertIn(response.data, [b'35%'])
    def test_Leo11(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Leo", "second_sign":"Aquarius"})
        self.assertIn(response.data, [b'68%'])
    def test_Leo12(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Leo", "second_sign":"Pisces"})
        self.assertIn(response.data, [b'38%'])

#Virgo
    def test_Virgo1(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Virgo", "second_sign":"Aries"})
        self.assertIn(response.data, [b'63%'])
    def test_Virgo2(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Virgo", "second_sign":"Taurus"})
        self.assertIn(response.data, [b'90%'])
    def test_Virgo3(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Virgo", "second_sign":"Gemini"})
        self.assertIn(response.data, [b'68%'])
    def test_Virgo4(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Virgo", "second_sign":"Cancer"})
        self.assertIn(response.data, [b'90%'])
    def test_Virgo5(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Virgo", "second_sign":"Leo"})
        self.assertIn(response.data, [b'35%'])
    def test_Virgo6(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Virgo", "second_sign":"Virgo"})
        self.assertIn(response.data, [b'65%'])
    def test_Virgo7(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Virgo", "second_sign":"Libra"})
        self.assertIn(response.data, [b'68%'])
    def test_Virgo8(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Virgo", "second_sign":"Scorpio"})
        self.assertIn(response.data, [b'88%'])
    def test_Virgo9(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Virgo", "second_sign":"Sagittarius"})
        self.assertIn(response.data, [b'48%'])
    def test_Virgo10(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Virgo", "second_sign":"Capricorn"})
        self.assertIn(response.data, [b'95%'])
    def test_Virgo11(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Virgo", "second_sign":"Aquarius"})
        self.assertIn(response.data, [b'30%'])
    def test_Virgo12(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Virgo", "second_sign":"Pisces"})
        self.assertIn(response.data, [b'88%'])


#Libra
    def test_Libra1(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Libra", "second_sign":"Aries"})
        self.assertIn(response.data, [b'85%'])
    def test_Libra2(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Libra", "second_sign":"Taurus"})
        self.assertIn(response.data, [b'65%'])
    def test_Libra3(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Libra", "second_sign":"Gemini"})
        self.assertIn(response.data, [b'93%'])
    def test_Libra4(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Libra", "second_sign":"Cancer"})
        self.assertIn(response.data, [b'43%'])
    def test_Libra5(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Libra", "second_sign":"Leo"})
        self.assertIn(response.data, [b'97%'])
    def test_Libra6(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Libra", "second_sign":"Virgo"})
        self.assertIn(response.data, [b'68%'])
    def test_Libra7(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Libra", "second_sign":"Libra"})
        self.assertIn(response.data, [b'75%'])
    def test_Virgo8(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Libra", "second_sign":"Scorpio"})
        self.assertIn(response.data, [b'35%'])
    def test_Libra9(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Libra", "second_sign":"Sagittarius"})
        self.assertIn(response.data, [b'73%'])
    def test_Libra10(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Libra", "second_sign":"Capricorn"})
        self.assertIn(response.data, [b'55%'])
    def test_Libra11(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Libra", "second_sign":"Aquarius"})
        self.assertIn(response.data, [b'90%'])
    def test_Libra12(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Libra", "second_sign":"Pisces"})
        self.assertIn(response.data, [b'88%'])


#Scorpio
    def test_Scorpio1(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Scorpio", "second_sign":"Aries"})
        self.assertIn(response.data, [b'50%'])
    def test_Scorpio2(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Scorpio", "second_sign":"Taurus"})
        self.assertIn(response.data, [b'88%'])
    def test_Scorpio3(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Scorpio", "second_sign":"Gemini"})
        self.assertIn(response.data, [b'28%'])
    def test_Scorpio4(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Scorpio", "second_sign":"Cancer"})
        self.assertIn(response.data, [b'94%'])
    def test_Scorpio5(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Scorpio", "second_sign":"Leo"})
        self.assertIn(response.data, [b'58%'])
    def test_Scorpio6(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Scorpio", "second_sign":"Virgo"})
        self.assertIn(response.data, [b'88%'])
    def test_Scorpio7(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Scorpio", "second_sign":"Libra"})
        self.assertIn(response.data, [b'35%'])
    def test_Scorpio8(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Scorpio", "second_sign":"Scorpio"})
        self.assertIn(response.data, [b'80%'])
    def test_Scorpio9(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Scorpio", "second_sign":"Sagittarius"})
        self.assertIn(response.data, [b'28%'])
    def test_Scorpio10(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Scorpio", "second_sign":"Capricorn"})
        self.assertIn(response.data, [b'95%'])
    def test_Scorpio11(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Scorpio", "second_sign":"Aquarius"})
        self.assertIn(response.data, [b'73%'])
    def test_Scorpio12(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Scorpio", "second_sign":"Pisces"})
        self.assertIn(response.data, [b'97%'])


#Scorpio
    def test_Sagittarius1(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Sagittarius", "second_sign":"Aries"})
        self.assertIn(response.data, [b'93%'])
    def test_Sagittarius2(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Sagittarius", "second_sign":"Taurus"})
        self.assertIn(response.data, [b'30%'])
    def test_Sagittarius3(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Sagittarius", "second_sign":"Gemini"})
        self.assertIn(response.data, [b'60%'])
    def test_Sagittarius4(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Sagittarius", "second_sign":"Cancer"})
        self.assertIn(response.data, [b'53%'])
    def test_Sagittarius5(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Sagittarius", "second_sign":"Leo"})
        self.assertIn(response.data, [b'93%'])
    def test_Sagittarius6(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Sagittarius", "second_sign":"Virgo"})
        self.assertIn(response.data, [b'48%'])
    def test_Sagittarius7(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Sagittarius", "second_sign":"Libra"})
        self.assertIn(response.data, [b'73%'])
    def test_Sagittarius8(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Sagittarius", "second_sign":"Scorpio"})
        self.assertIn(response.data, [b'28%'])
    def test_Sagittarius9(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Sagittarius", "second_sign":"Sagittarius"})
        self.assertIn(response.data, [b'45%'])
    def test_Sagittarius10(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Sagittarius", "second_sign":"Capricorn"})
        self.assertIn(response.data, [b'60%'])
    def test_Sagittarius11(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Sagittarius", "second_sign":"Aquarius"})
        self.assertIn(response.data, [b'90%'])
    def test_Sagittarius12(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Sagittarius", "second_sign":"Pisces"})
        self.assertIn(response.data, [b'63%'])



#Capricorn
    def test_Capricorn1(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Capricorn", "second_sign":"Aries"})
        self.assertIn(response.data, [b'47%'])
    def test_Capricorn2(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Capricorn", "second_sign":"Taurus"})
        self.assertIn(response.data, [b'98%'])
    def test_Capricorn3(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Capricorn", "second_sign":"Gemini"})
        self.assertIn(response.data, [b'68%'])
    def test_Capricorn4(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Capricorn", "second_sign":"Cancer"})
        self.assertIn(response.data, [b'83%'])
    def test_Capricorn5(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Capricorn", "second_sign":"Leo"})
        self.assertIn(response.data, [b'35%'])
    def test_Capricorn6(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Capricorn", "second_sign":"Virgo"})
        self.assertIn(response.data, [b'95%'])
    def test_Capricorn7(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Capricorn", "second_sign":"Libra"})
        self.assertIn(response.data, [b'55%'])
    def test_Capricorn8(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Capricorn", "second_sign":"Scorpio"})
        self.assertIn(response.data, [b'95%'])
    def test_Capricorn9(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Capricorn", "second_sign":"Sagittarius"})
        self.assertIn(response.data, [b'60%'])
    def test_Capricorn10(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Capricorn", "second_sign":"Capricorn"})
        self.assertIn(response.data, [b'75%'])
    def test_Capricorn11(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Capricorn", "second_sign":"Aquarius"})
        self.assertIn(response.data, [b'68%'])
    def test_Capricorn12(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Capricorn", "second_sign":"Pisces"})
        self.assertIn(response.data, [b'88%'])

#Aquarius
    def test_Aquarius1(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aquarius", "second_sign":"Aries"})
        self.assertIn(response.data, [b'78%'])
    def test_Aquarius2(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aquarius", "second_sign":"Taurus"})
        self.assertIn(response.data, [b'58%'])
    def test_Aquarius3(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aquarius", "second_sign":"Gemini"})
        self.assertIn(response.data, [b'85%'])
    def test_Aquarius4(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aquarius", "second_sign":"Cancer"})
        self.assertIn(response.data, [b'27%'])
    def test_Aquarius5(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aquarius", "second_sign":"Leo"})
        self.assertIn(response.data, [b'68%'])
    def test_Aquarius6(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aquarius", "second_sign":"Virgo"})
        self.assertIn(response.data, [b'30%'])
    def test_Aquarius7(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aquarius", "second_sign":"Libra"})
        self.assertIn(response.data, [b'90%'])
    def test_Aquarius8(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aquarius", "second_sign":"Scorpio"})
        self.assertIn(response.data, [b'73%'])
    def test_Aquarius9(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aquarius", "second_sign":"Sagittarius"})
        self.assertIn(response.data, [b'90%'])
    def test_Aquarius10(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aquarius", "second_sign":"Capricorn"})
        self.assertIn(response.data, [b'68%'])
    def test_Aquarius11(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aquarius", "second_sign":"Aquarius"})
        self.assertIn(response.data, [b'45%'])
    def test_Aquarius12(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Aquarius", "second_sign":"Pisces"})
        self.assertIn(response.data, [b'45%'])



#Pisces
    def test_Pisces1(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Pisces", "second_sign":"Aries"})
        self.assertIn(response.data, [b'67%'])
    def test_Pisces2(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Pisces", "second_sign":"Taurus"})
        self.assertIn(response.data, [b'85%'])
    def test_Pisces3(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Pisces", "second_sign":"Gemini"})
        self.assertIn(response.data, [b'53%'])
    def test_Pisces4(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Pisces", "second_sign":"Cancer"})
        self.assertIn(response.data, [b'98%'])
    def test_Pisces5(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Pisces", "second_sign":"Leo"})
        self.assertIn(response.data, [b'38%'])
    def test_Pisces6(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Pisces", "second_sign":"Virgo"})
        self.assertIn(response.data, [b'88%'])
    def test_Pisces7(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Pisces", "second_sign":"Libra"})
        self.assertIn(response.data, [b'85%'])
    def test_Pisces8(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Pisces", "second_sign":"Scorpio"})
        self.assertIn(response.data, [b'97%'])
    def test_Pisces9(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Pisces", "second_sign":"Sagittarius"})
        self.assertIn(response.data, [b'63%'])
    def test_Pisces10(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Pisces", "second_sign":"Capricorn"})
        self.assertIn(response.data, [b'88%'])
    def test_Pisces11(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Pisces", "second_sign":"Aquarius"})
        self.assertIn(response.data, [b'45%'])
    def test_Pisces12(self):
        response=self.client.post(url_for("description"), json={"first_sign":"Pisces", "second_sign":"Pisces"})
        self.assertIn(response.data, [b'60%'])