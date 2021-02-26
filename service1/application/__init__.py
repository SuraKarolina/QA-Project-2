from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv


app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DB_URI")
app.config['SECRET_KEY'] = getenv("SC_KEY")

db = SQLAlchemy(app)


from application import routes
