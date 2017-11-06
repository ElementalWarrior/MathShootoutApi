# Import flask and template operators
from flask import Flask, render_template, request, g
import os

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.orm import scoped_session, sessionmaker

# Define the WSGI application object
app = Flask(__name__)

# Configurations
# app.config.from_object('config')

DB_URL = 'postgres://kffjeqxcfybuqw:1f9b9331d78c00ea9732f930b5cd75b1e9bb950a8f5eaa5b0862b89e562bebb6@ec2-54-243-55-1.compute-1.amazonaws.com:5432/de1covhitb2945'
# DB_URL = os.environ['DATABASE_URI']
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return "404 Not Found", 404

@app.route('/')
def index():
	return ""

@app.route('/submit', methods=['POST'])
def submit():
	# get raw post body
	# print(request.data)

	# get post body as json
	obj = request.get_json()
	# print request
	# print obj
	res = db.session.execute('''
		insert into
		logs (
			session_id
			, player_name
			, date_session_start
			, tag
			, data
			, date_created
		)
		values
			(:session_id
			, :player_name
			, :date_session_start
			, :tag
			, :data
			, :date_created)
	''', {
	'session_id': obj['session_id']
	, 'player_name': obj['player_name']
	, 'date_session_start': obj['date_session_start']
	, 'tag': obj['tag']
	, 'data': obj['data']
	, 'date_created': obj['date_created']
	})
	db.session.commit()
	return ''
