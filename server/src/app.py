from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from firebase_admin import credentials, firestore, initialize_app
import os
import time

app = Flask(__name__, static_folder='')

cred = credentials.Certificate("key.json")
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('todos')


# @app.route('/', methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         return render_template('index.html')
#     else:
#         return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/directory')
def directory():
    return render_template('directory.html')


@app.route('/jobs')
def jobs():
    return render_template('jobs.html')


@app.route('/resources')
def resources():
    return render_template('resources.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/forgotpassword')
def forgotpassword():
    return render_template('forgotpassword.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/postjoblisting')
def postjoblisting():
    return render_template('postjoblisting.html')


@app.route('/postservices')
def postservices():
    return render_template('postservices.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=int(os.environ.get('PORT', 8080)))
