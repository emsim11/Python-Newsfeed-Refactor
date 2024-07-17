# Corresponds To Index.js File of Node.js Module

from flask import Flask
from App.Routes import Home, Dashboard
from App.Database import Init_Database
from App.Utilities import Filters

def create_app(test_config=None):
  # Setup App Configuration
  App = Flask(__name__, static_url_path='/')
  App.url_map.strict_slashes = False
  App.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )
  
  # Inner Function `Hello()` Returns A String
  @App.route('/hello')
  def Hello():
    return 'Hello World! 🌈'
  
  # Register Routes
  App.register_blueprint(Home)
  App.register_blueprint(Dashboard)
  
  # Register Custom Filter Functions
  App.jinja_env.filters['Format_URL'] = Filters.Format_URL
  App.jinja_env.filters['Format_Date'] = Filters.Format_Date
  App.jinja_env.filters['Format_Plural'] = Filters.Format_Plural
  
  # Setup Database Connection In Flask App
  Init_Database(App)
  
  return App