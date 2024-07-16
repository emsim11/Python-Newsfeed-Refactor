from flask import Blueprint, render_template

Blueprints = Blueprint('home', __name__, url_prefix='/')

@Blueprints.route('/')
def index():
  return render_template('homepage.html')

@Blueprints.route('/login')
def login():
  return render_template('login.html')

@Blueprints.route('/post/<id>')
def single(id):
  return render_template('single-post.html')