import unittest
from flask import url_for
from flask_testing import TestCase
from os import getenv
import requests_mock

from application import app, db
from application.models import Match

class Testbase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv("DATABASE_URI2"),
            DEBUG=True, WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        test_character=Character(Character_class="Paladin", Character_race="Gnomish", Character_description="Super evil")
        db.session.add(test_character)
        db.session.commit()
        
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()


