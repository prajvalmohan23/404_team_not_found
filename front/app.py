import flask
from flask_mongoengine import MongoEngine
import requests
import os
import json
from flask import Flask, request, jsonify, session, flash, redirect, url_for, render_template
from dotenv import load_dotenv

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
app.config['SECRET_KEY'] = 'GDtfDCFYjD'
db.init_app(app)


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/createitem')
def createitem():
    return render_template('createitem.html')

@app.route('/modifyitem')
def modifyitem():
    return render_template('modifyitem.html')

@app.route('/createcategory')
def createcategory():
    return render_template('createcategory.html')

@app.route('/modifycategory')
def modifycategory():
    return render_template('modifycategory.html')

@app.route('/updateUser')
def updateUser():
    return render_template('updateUser.html')

@app.route('/receiveSupport')
def receiveSupport():
    return render_template('receiveSupport.html')

@app.route('/loginUser', methods=['POST'])
def loginUser():
    form = request.form
    params = {
        'user_name': form['uname'],
        'password': form['psw']
    }
    resp = requests.post("http://service.user:5000/login",params=params)
    if resp.json()['status_code'] == "200":
        session['user'] = resp.json()["detail"]["user_id"]
        return redirect(url_for('home'))
    else:
        # flash('Incorrect credentials')
        return redirect(url_for('login'))


@app.route('/logoutUser', methods=['POST','GET'])
def logoutUser():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    # app.run()
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)