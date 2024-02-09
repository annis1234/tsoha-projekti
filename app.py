from flask import Flask,render_template, request, jsonify, session, redirect
from sqlalchemy.sql import text
from os import getenv

app = Flask(__name__)
app.secret_key=getenv("SECRET_KEY")

import routes
