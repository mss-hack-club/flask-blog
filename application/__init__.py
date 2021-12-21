from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app=app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

from application import routes
