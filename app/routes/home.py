from flask import Blueprint, render_template

Blueprints = Blueprint('Home', __name__, url_prefix='/')

@Blueprints.route('/')
def Index():
  return render_template('Homepage.html')

@Blueprints.route('/Login')
def Login():
  return render_template('Login.html')

@Blueprints.route('/Post/<id>')
def Single(id):
  return render_template('Single-Post.html')