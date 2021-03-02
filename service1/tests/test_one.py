import unittest
from flask import url_for
from flask_testing import TestCase
from os import getenv
import requests_mock

from application import app, db
from application.models import Match

class Testbase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
        SECRET_KEY=getenv('TEST_SECRET_KEY'),
        WTF_CSRF_ENABLED=False,
        DEBUG=True
        )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

        test_match = Match(first_sign = 'Aquarius', second_sign = 'Pisces', description = '45%')
        db.session.add(test_match)
        db.session.commit()
        
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestCreate(Testbase):
    def test_char(self):
        with requests_mock.mock() as r:
            r.get("http://localhost:5001/first_sign", text='Aquarius')
            r.get("http://localhost:5002/second_sign", text='Pisces')
            r.get("http://localhost:5003/description", text='45%')
            response=self.client.get(url_for('home'))
            self.assertEqual(response.status_code,200)
            self.assertIn(b'You have generated Aquarius and Pisces', response.data)
            self.assertIn(b'Their friendship match is 45%', response.data)

