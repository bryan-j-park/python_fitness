from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user_models import User


class Record:
  def __init__(self, data):
    self.id = data['id']
    self.date = data['date']
    self.food = data['food']
    self.meal = data['meal']
    self.calories = data['calories_cal']
    self.carbs = data['carbs_g']
    self.fat = data['fat_g']
    self.protein = data['protein_g']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.user_id = data['user_id']

#adds data to the database and saves it under the spedific user
  @classmethod
  def add_food(cls, data):
    query = 'INSERT INTO records (date, food, meal, calories_cal, carbs_g, fat_g, protein_g, created_at, updated_at, user_id) VALUES (%(date)s, %(food)s, %(meal)s, %(calories)s, %(carbs)s, %(fat)s, %(protein)s, NOW(), NOW(), %(user_id)s);'
    return connectToMySQL('python_fitness').query_db(query, data)

#get all saved info pertaining to a specific user
  @classmethod
  def get_saved_food(cls, data):
    query = 'SELECT * FROM records WHERE user_id = %(id)s'
    results = connectToMySQL('python_fitness').query_db(query, data)
    foods = []
    for dict in results:
      food = cls(dict)
      foods.append(food)
    return foods

#getting all the data the user saved, sorting and grouping by date
  @classmethod
  def get_all_by_date(cls, data):
    query = 'SELECT date, sum(calories_cal), sum(carbs_g), sum(fat_g), sum(protein_g) FROM records WHERE user_id = %(id)s GROUP BY date ORDER BY date desc;'
    return connectToMySQL('python_fitness').query_db(query, data)

#getting one day data and adding it all together 
  @classmethod
  def get_one_by_date(cls, data):
    query = 'SELECT date, sum(calories_cal), sum(carbs_g), sum(fat_g), sum(protein_g) FROM records WHERE user_id = %(id)s AND date = %(date)s;'
    return connectToMySQL('python_fitness').query_db(query, data)

#gets all the information from a specific date and user
  @classmethod
  def get_by_specific_date(cls, data):
    query = 'SELECT * FROM records WHERE user_id = %(id)s AND date = %(date)s;'
    results = connectToMySQL('python_fitness').query_db(query, data)
    foods = []
    for dict in results:
      food = cls(dict)
      foods.append(food)
    return foods

#removes a single food item from the database
  @classmethod
  def remove_data(cls, data):
    query = 'DELETE FROM records WHERE id = %(id)s;'
    return connectToMySQL('python_fitness').query_db(query, data)

#sorting all the food by various categories and amounts
  @classmethod
  def order_by_date(cls, data):
    query = 'SELECT * FROM records WHERE user_id = %(id)s ORDER BY date;'
    results = connectToMySQL('python_fitness').query_db(query, data)
    foods = []
    for dict in results:
      food = cls(dict)
      foods.append(food)
    return foods

  @classmethod
  def order_by_meal(cls, data):
    query = 'SELECT * FROM records WHERE user_id = %(id)s ORDER BY meal;'
    results = connectToMySQL('python_fitness').query_db(query, data)
    foods = []
    for dict in results:
      food = cls(dict)
      foods.append(food)
    return foods

  @classmethod
  def order_by_lowest_cal(cls, data):
    query = 'SELECT * FROM records WHERE user_id = %(id)s ORDER BY calories_cal;'
    results = connectToMySQL('python_fitness').query_db(query, data)
    foods = []
    for dict in results:
      food = cls(dict)
      foods.append(food)
    return foods

  @classmethod
  def order_by_highest_cal(cls, data):
    query = 'SELECT * FROM records WHERE user_id = %(id)s ORDER BY calories_cal DESC;'
    results = connectToMySQL('python_fitness').query_db(query, data)
    foods = []
    for dict in results:
      food = cls(dict)
      foods.append(food)
    return foods

  @classmethod
  def order_by_lowest_carb(cls, data):
    query = 'SELECT * FROM records WHERE user_id = %(id)s ORDER BY carbs_g;'
    results = connectToMySQL('python_fitness').query_db(query, data)
    foods = []
    for dict in results:
      food = cls(dict)
      foods.append(food)
    return foods

  @classmethod
  def order_by_highest_carb(cls, data):
    query = 'SELECT * FROM records WHERE user_id = %(id)s ORDER BY carbs_g DESC;'
    results = connectToMySQL('python_fitness').query_db(query, data)
    foods = []
    for dict in results:
      food = cls(dict)
      foods.append(food)
    return foods

  @classmethod
  def order_by_lowest_fat(cls, data):
    query = 'SELECT * FROM records WHERE user_id = %(id)s ORDER BY fat_g;'
    results = connectToMySQL('python_fitness').query_db(query, data)
    foods = []
    for dict in results:
      food = cls(dict)
      foods.append(food)
    return foods

  @classmethod
  def order_by_highest_fat(cls, data):
    query = 'SELECT * FROM records WHERE user_id = %(id)s ORDER BY fat_g DESC;'
    results = connectToMySQL('python_fitness').query_db(query, data)
    foods = []
    for dict in results:
      food = cls(dict)
      foods.append(food)
    return foods

  @classmethod
  def order_by_lowest_protein(cls, data):
    query = 'SELECT * FROM records WHERE user_id = %(id)s ORDER BY protein_g;'
    results = connectToMySQL('python_fitness').query_db(query, data)
    foods = []
    for dict in results:
      food = cls(dict)
      foods.append(food)
    return foods

  @classmethod
  def order_by_highest_protein(cls, data):
    query = 'SELECT * FROM records WHERE user_id = %(id)s ORDER BY protein_g DESC;'
    results = connectToMySQL('python_fitness').query_db(query, data)
    foods = []
    for dict in results:
      food = cls(dict)
      foods.append(food)
    return foods

  @staticmethod
  def validate_food(data):
    is_valid = True

    if len(data['food']) < 3:
      flash('Food name must be at least 3 characters long', 'nutrition')
      is_valid = False

    if len(data['calories']) < 1:
      flash('Calories must be added', 'nutrition')
      is_valid = False

    if len(data['fat']) < 1:
      flash('Fat must be calculated', 'nutrition')
      is_valid = False

    if len(data['carbs']) < 1:
      flash('Carbs must be calculated', 'nutrition')
      is_valid = False

    if len(data['protein']) < 1:
      flash('Protein must be calculated', 'nutrition')
      is_valid = False

    if len(data['date']) < 1:
      flash('Date must be selected', 'nutrition')
      is_valid = False

    if len(data['meal']) < 1:
      flash('Meal must be selected', 'nutrition')
      is_valid = False

    return is_valid