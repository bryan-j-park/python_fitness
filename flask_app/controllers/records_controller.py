from flask_app import app
from flask_app.models.record_models import Record
from flask_app.models.user_models import User
from flask import render_template, redirect, request, session, flash, jsonify
import requests #remember to do pipenv install requests
import os


# Calls the Edamam API 
@app.route('/call_api', methods = ["POST"])
def call_api():

  if request.form['amount'] == "" or request.form['ingr'] == "":
    return redirect('/dashboard')

  api_id = os.environ.get('API_ID')
  api_key = os.environ.get('API_KEY')
  cooking = request.form['nutritionType']
  amount = request.form['amount']
  ingredients = request.form['ingr']

  if(request.form['measurement'] == "null"):
    api_request = requests.get(f'https://api.edamam.com/api/nutrition-data?app_id={api_id}&app_key={api_key}&nutrition-type={cooking}&ingr={amount}%20{ingredients}')
    return jsonify(api_request.json())
  else:
    measurement = request.form['measurement']
    api_request = requests.get(f'https://api.edamam.com/api/nutrition-data?app_id={api_id}&app_key={api_key}&nutrition-type={cooking}&ingr={amount}%20{measurement}%20{ingredients}')
    return jsonify(api_request.json())

@app.route('/records')
def saved_foods():
  if 'user_id' not in session:
    return redirect('/')

  user_data = {
    'id': session['user_id']
  }
  user = User.get_user_by_id(user_data)
  foods = Record.get_saved_food(user_data)
  return render_template('saved_food.html', user = user, foods = foods)

@app.route('/calculator')
def calculator_page():
  return render_template('calculator.html')

@app.route('/saved_by_date')
def get_by_date():
  if 'user_id' not in session:
    return redirect('/')

  user_data = {
    'id': session['user_id']
  }
  user = User.get_user_by_id(user_data)
  foods = Record.get_all_by_date(user_data)
  return render_template('saved_by_date.html', user = user, foods = foods)

@app.route('/save_food', methods = ['POST'])
def save_food():
  if not Record.validate_food(request.form):
    return redirect(request.referrer)

  data = {
    **request.form,
    'user_id': session['user_id']
  }

  Record.add_food(data)
  return redirect('/records')


@app.route('/single_day/<date>')
def sort_by_single_day(date):
  if 'user_id' not in session:
    redirect('/')

  user_data = {
    'id': session['user_id']
  }
  user = User.get_user_by_id(user_data)

  data = {
    'id': session['user_id'],
    'date': date
  }
  date = date
  foods = Record.get_by_specific_date(data)
  totals = Record.get_one_by_date(data)
  return render_template('single_day.html', user = user, foods = foods, date = date, totals = totals)

@app.route('/remove/<int:num>')
def remove(num):
  data = {
    'id': num
  }
  Record.remove_data(data)
  return redirect(request.referrer)

#Sorted app.route in order to sort data by specific information
@app.route('/sort_by', methods = ['POST'])
def sort_by():
  if 'user_id' not in session:
    return redirect('/')

  session['choice'] = request.form['choice']
  if session['choice'] == 'none':
    return redirect('/records')
  return redirect('/sortted')

@app.route('/sortted')
def sort_query():
  if 'user_id' not in session:
    return redirect('/')
  
  user_data = {
    'id': session['user_id']
  }
  user = User.get_user_by_id(user_data)
  
  if session['choice'] == 'newest':
    foods = Record.get_saved_food(user_data)
    session.pop('choice')
    sort_by = 'Sorted By Newest'
    return render_template('sorted_by.html', user = user, foods = foods, sort_by = sort_by)
  
  elif session['choice'] == 'oldest':
    foods = Record.order_by_date(user_data)
    session.pop('choice')
    sort_by = 'Sorted By Oldest'
    return render_template('sorted_by.html', user = user, foods = foods, sort_by = sort_by)
  
  elif session['choice'] == 'meal':
    foods = Record.order_by_meal(user_data)
    session.pop('choice')
    sort_by = 'Sorted By Meals'
    return render_template('sorted_by.html', user = user, foods = foods, sort_by = sort_by)
  
  elif session['choice'] == 'lowest_cal':
    foods = Record.order_by_lowest_cal(user_data)
    session.pop('choice')
    sort_by = 'Sorted By Lowest Calories'
    return render_template('sorted_by.html', user = user, foods = foods, sort_by = sort_by)
  
  elif session['choice'] == 'highest_cal':
    foods = Record.order_by_highest_cal(user_data)
    session.pop('choice')
    sort_by = 'Sorted By Highest Calories'
    return render_template('sorted_by.html', user = user, foods = foods, sort_by = sort_by)
  
  elif session['choice'] == 'lowest_carb':
    foods = Record.order_by_lowest_carb(user_data)
    session.pop('choice')
    sort_by = 'Sorted By Lowest Carbs'
    return render_template('sorted_by.html', user = user, foods = foods, sort_by = sort_by)
  
  elif session['choice'] == 'highest_carb':
    foods = Record.order_by_highest_carb(user_data)
    session.pop('choice')
    sort_by = 'Sorted By Highest Carbs'
    return render_template('sorted_by.html', user = user, foods = foods, sort_by = sort_by)
  
  elif session['choice'] == 'lowest_fat':
    foods = Record.order_by_lowest_fat(user_data)
    session.pop('choice')
    sort_by = 'Sorted By Lowest Fat'
    return render_template('sorted_by.html', user = user, foods = foods, sort_by = sort_by)
  
  elif session['choice'] == 'highest_fat':
    foods = Record.order_by_highest_fat(user_data)
    session.pop('choice')
    sort_by = 'Sorted By Highest Fat'
    return render_template('sorted_by.html', user = user, foods = foods, sort_by = sort_by)
  
  elif session['choice'] == 'lowest_prot':
    foods = Record.order_by_lowest_protein(user_data)
    session.pop('choice')
    sort_by = 'Sorted By Lowest Protein'
    return render_template('sorted_by.html', user = user, foods = foods, sort_by = sort_by)
  
  elif session['choice'] == 'highest_prot':
    foods = Record.order_by_highest_protein(user_data)
    session.pop('choice')
    sort_by = 'Sorted By Highest Protein'
    return render_template('sorted_by.html', user = user, foods = foods, sort_by = sort_by)



