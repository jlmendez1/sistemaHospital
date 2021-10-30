from flask import Flask, abort, redirect, url_for, flash, session
#from .dotenv import load_dotenv
from os import environ
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#load_dotenv()

#PORT = int(environ["PORT"])
PORT = 3500

app = Flask(__name__)

#-------------LLave secreta del sistema--------------
app.secret_key= os.urandom(24)
#-------Conexion a OMR para base de datos-------------
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:jorl2001@localhost/sistemahospital'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
ma = Marshmallow(app)
#------------------------------------------------------


# import declared routes
from app.routes import *

