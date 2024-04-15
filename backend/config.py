from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# init app
app = Flask(__name__)
CORS(app) # disable cors related error

# db config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # not track all changes

# create db instance
db = SQLAlchemy(app)