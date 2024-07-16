# Corresponds To Index.js File of Node.js Module

from flask import Flask
from App.Routes import Home, Dashboard

def create_app(test_config=None):
  # Setup App Configuration
  App = Flask(__name__, static_url_path='/')
  App.url_map.strict_slashes = False
  App.config.from_mapping(
    SECRET_KEY='Super_Secret_Key'
  )
  
  @App.route('/hello')
  def Hello():
    return 'Hello World! 🌈'
  
  # Register Routes
  App.register_blueprint(Home)
  App.register_blueprint(Dashboard)
  
  return App