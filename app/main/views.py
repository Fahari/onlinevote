from flask import render_template
from . import main
from flask_login import login_required
import requests
from .. import db

#views
@main.route("/")
def index():
	'''
	This is the index
	'''


	return render_template('index.html' )
