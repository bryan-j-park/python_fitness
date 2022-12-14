#change file name to name of table in database
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

#create class and classmethods
class User:
  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.email = data['email']
    self.password = data['password']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

#query to register a new user to the database
  @classmethod
  def register_user(cls, data):
    query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());'
    return connectToMySQL('python_fitness').query_db(query, data)

#queries the database in order get a user by the id 
  @classmethod
  def get_user_by_id(cls, data):
    query = 'SELECT * FROM users WHERE id = %(id)s;'
    result = connectToMySQL('python_fitness').query_db(query, data)
    return cls(result[0])

#queries the database for an email matching the data provided and if one is not present then will return false 
  @classmethod 
  def get_by_email(cls, data):
    query = 'SELECT * FROM users WHERE email = %(email)s'
    result = connectToMySQL('python_fitness').query_db(query, data)
    if len(result) < 1:
      return False
    return cls(result[0])

#this is used to validate the user while registering 
  @staticmethod
  def validate_registration(data):
    is_valid = True

#if first name is too short it will flash an erroe message
    if len(data['first_name']) < 2:
      flash('First name must be at least 2 characters long', 'register')
      is_valid = False

#if last name is too short it will flash an error message
    if len(data['last_name']) < 2: 
      flash('Last name must be at least 2 characters long', 'register')
      is_valid = False

#checks to see if the email is in valid email formation ex:"hello@hello.com"
    if not EMAIL_REGEX.match(data['email']):
      flash('Invalid email address', 'register')
      is_valid = False

#checks to see if the email is already registered with the database, if it is, the user cant register.
    query = 'SELECT * FROM users WHERE email = %(email)s'
    result = connectToMySQL('python_fitness').query_db(query, data)
    if len(result) >= 1:
      flash('Email unavailable', 'register')
      is_valid = False

#checks to make sure the password is a certain length
    if len(data['password']) < 8:
      flash('Password must be at least 8 characters long', 'register')
      is_valid = False

#checks to see if the password and confirm password match
    if data['password'] != data['confirm_password']:
      flash('Password does not match confirm password', 'register')
      is_valid = False
    return is_valid