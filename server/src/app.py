from flask import Flask, render_template, request, redirect, session
from firebase_admin import credentials, initialize_app
from functools import wraps
import os
import pyrebase

app = Flask(__name__, static_folder='')
app.config['SESSION_TYPE'] = 'memcached'
app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)

config = {
  "apiKey": "AIzaSyC3-64_FCq0MTfkz1yZxPgiMg6FjekjsyQ",
  "authDomain": "ecobiz-com.firebaseapp.com",
  "projectId": "ecobiz-com",
  "storageBucket": "ecobiz-com.appspot.com",
  "messagingSenderId": "530286252060",
  "appId": "1:530286252060:web:febfb512972936c9d94fd9",
  "measurementId": "G-KY5ZQDXGFB",
  "databaseURL": "https://ecobiz-com-default-rtdb.firebaseio.com/"
}

cred = credentials.Certificate("key.json")
default_app = initialize_app(cred)
# db = firestore.client()
pb = pyrebase.initialize_app(config)

auth = pb.auth()
db = pb.database()


def check_token(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        try:
            user = auth.current_user
        except:
            return redirect('https://ecobiz-com.web.app/login')
        return f(*args, **kwargs)
    return wrap


@app.route('/')
def index():
    user = ""
    try:
        user = session['usr']
    except:
        pass
    return render_template('index.html', req=auth.current_user)


@app.route('/directory')
def directory():
    services = db.child("services").get().val()
    service_list = []
    service_row = []
    for service in services:
        service_row.append(services[service])
        if len(service_row) == 3:
            service_list.append(service_row)
            service_row = []
    service_list.append(service_row)
    return render_template('directory.html', service_list=service_list)


@app.route('/jobs')
def jobs():
    job_listings = db.child("joblistings").get().val()
    jobs_list = []
    jobs_row = []
    for job in job_listings:
        jobs_row.append(job_listings[job])
        if len(jobs_row) == 3:
            jobs_list.append(jobs_row)
            jobs_row = []
    jobs_list.append(jobs_row)
    return render_template('jobs.html', jobs_list=jobs_list)


@app.route('/resources')
def resources():
    return render_template('resources.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email is None or password is None:
            return render_template('login.html', error="Error missing email or password")
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            auth.refresh(user['refreshToken'])
            return redirect('https://ecobiz-com.web.app/')
        except Exception as e:
            return render_template('login.html', error="Error logging in<br />{}".format(e))
    return render_template('login.html')


@app.route('/logout')
def logout():
    auth.signOut()
    try:
        session.pop('usr', None)
    except:
        pass
    return redirect('https://ecobiz-com.web.app/')


@app.route('/forgotpassword')
def forgotpassword():
    return render_template('forgotpassword.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email is None or password is None:
            return render_template('register.html', error="Error missing email or password")
        elif len(password) < 6:
            return render_template('register.html', error="Password must be greater than 6 characters", email=email)
        try:
            user = auth.create_user_with_email_and_password(email, password)
            auth.refresh(user['refreshToken'])
            return redirect('https://ecobiz-com.web.app/')
        except Exception as e:
            return render_template('register.html', error="Error creating user<br />{}".format(e))
    return render_template('register.html')


@app.route('/postjoblisting', methods=['POST', 'GET'])
@check_token
def postjoblisting():
    if request.method == 'POST':
        company = request.form.get('company', "No company anem")
        jobTitle = request.form.get('jobTitle', "No job title")
        skills_needed = request.form.get('skills-needed', "No skills needed")
        description = request.form.get('description', "No description")
        website = request.form.get('website', "No website")
        linkedin = request.form.get('linkedin', "No LinkedIn")
        instagram = request.form.get('instagram', "No Instagram")
        application = request.form.get('application', "No application")
        img = request.form.get('img', '/images/weavegrid.png')
        data = {
            "application": application,
            "company": company,
            "jobTitle": jobTitle,
            "description": description,
            "website": website,
            "linkedin": linkedin,
            "instagram": instagram,
            "skills_needed": skills_needed,
            "img": img
        }
        try:
            db.child("joblistings").push(data)
            return redirect('https://ecobiz-com.web.app/directory')
        except Exception as e:
            return render_template('postjoblisting.html', error="Error creating listing<br />{}".format(e))
    return render_template('postjoblisting.html')


@app.route('/postservices', methods=['POST', 'GET'])
@check_token
def postservices():
    if request.method == 'POST':
        full_name = request.form.get('full-name', "No name")
        jobTitle = request.form.get('jobTitle', "No title")
        skills = request.form.get('skills', "No skills")
        bio = request.form.get('bio', "No bio")
        website = request.form.get('website', "No website")
        linkedin = request.form.get('linkedin', "No LinkedIn")
        instagram = request.form.get('instagram', "No Instagram")
        img = request.form.get('img', '/images/randyschleifer.png')
        data = {
            "full_name": full_name,
            "jobTitle": jobTitle,
            "skills": skills,
            "website": website,
            "linkedin": linkedin,
            "instagram": instagram,
            "bio": bio,
            "img": img
        }
        try:
            db.child("joblistings").push(data)
            return redirect('https://ecobiz-com.web.app/directory')
        except Exception as e:
            return render_template('postjoblisting.html', error="Error creating listing<br />{}".format(e))
    return render_template('postservices.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=int(os.environ.get('PORT', 8080)))
