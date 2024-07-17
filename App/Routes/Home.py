from flask import Blueprint, render_template
from App.Models import Post
from App.Database import Get_Database

# Use `Blueprint()` To Consolidate Routes Onto A Single `Blueprint` Object That Parent App Registers
Blueprints = Blueprint('Home', __name__, url_prefix='/')

# `Index()` Function Routes To `Homepage`
@Blueprints.route('/')
def Index():
  # Get All Posts
  Database = Get_Database()
  
  # Save Results In `Posts` Variable
  Posts = Database.query(Post).order_by(Post.Created_At.desc()).all()
  
  # Render Template With `Posts` Data
  return render_template('Homepage.html', Posts=Posts)

# `Login()` Function Routes To `Login`
@Blueprints.route('/login')
def Login():
  return render_template('Login.html')

# `<Id>` Route Parameter Becomes Function Parameter In `Single()` Function
@Blueprints.route('/post/<Id>')
def Single(Id):
  # Get Single Post By Id
  Database = Get_Database()
  Posts = Database.query(Post).filter(Post.Id == Id).one()
  
  # Render Single Post Template
  return render_template('Single-Post.html', Post=Posts)