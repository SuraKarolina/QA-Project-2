from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):

    def description_one(self):
        with patch('request.get') as i:
            i.return_value = 'Aries'
            with patch('request.get') as i:
                i.return_value = 'Aries'
                with patch('request.get') as i:
                    i.return_value = '50%'
                    response = self.client.post(
                    url_for('description'),
                    data = ('Aries', 'Aries'))
                    self.assertIn(b'50%', response.data)