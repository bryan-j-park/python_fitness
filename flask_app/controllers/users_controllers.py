#change file name before starting to name of singular model
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models.user_models import User
import requests
import os

@app.route('/')
def index():
  if 'user_id' in session:
    return redirect('/dashboard')
  return render_template('index.html')

@app.route('/dashboard')
def dashboard():
  if not 'user_id' in session:
    return redirect('/')
  data = {
    'id': session['user_id']
  }
  print(session['user_id'])
  user = User.get_user_by_id(data)
  print(user.first_name)
  return render_template('dashboard.html', user = user)

@app.route('/register')
def registration_page():
  return render_template('register.html')

@app.route('/login')
def login_page():
  return render_template('login.html')

#links to logout button and clears the session, then redirects to the login page 
@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')

#route to determine is the information provided is valid and creates a new user if all information is valid
@app.route('/register_user', methods = ['POST'])
def register():
#checks to see if the registration info is in valid format, if not then redirect to the main page
  if not User.validate_registration(request.form):
    return redirect('/register')

#generates the hash for the password, not allowing us to see the password when entered into the database
  pw_hash = bcrypt.generate_password_hash(request.form['password'])
  data = {
    **request.form,
    'password': pw_hash
  }

#saves the registration info into the database 
  user_id = User.register_user(data)

#creates a session['user_id] key and the value is based on the user id
  session['user_id'] = user_id
  return redirect('/')


#app route for logging into the website 
@app.route('/login_user', methods =['POST'])
def login():
#checks the database to see if the email entered into login form is present in the database
  data = {'email': request.form['email']}
  user_in_db = User.get_by_email(data)

#if the user email is not present in the database then it will flash an error message
  if not user_in_db:
    flash('Invalid Login Information', 'login')
    return redirect('/login')

#if the password is not present in the database then it will flash an error message
  if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
    flash('Invalid Login Information', 'login')
    return redirect('/login')

#creates a session once logged in, this creates a session['user_id'] based on the users id
  session['user_id'] = user_in_db.id
  return redirect('/')