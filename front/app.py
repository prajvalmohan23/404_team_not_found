import flask
from flask_mongoengine import MongoEngine
from flask import render_template
import requests
import os
import json
from flask import Flask, request, jsonify
from dotenv import load_dotenv
# from flask_sqlalchemy import SQLAlchemy

db = MongoEngine()
# connString = os.environ['MONGODB_CONNSTRING']   ### for docker uncomment
app = Flask(__name__)
# app.config["MONGODB_SETTINGS"] = [
#     {
#         "db": "item",
#         # "host": "localhost",               ### comment if docker
#         "host": connString,              ### comment if localhost
#         "port": 27017,
#         "alias": "core_item",
#     },
# ]
db.init_app(app)



@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

    



if __name__ == "__main__":
    # app.run()
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)