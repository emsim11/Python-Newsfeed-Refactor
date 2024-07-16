#__Init__.py File of Python Package Corresponds To Index.js File of Node.js Module
from flask import Flask
from App.Routes import Home

def create_app(test_config=None):
  # Setup App Configuration
  App = Flask(__name__, static_url_path='/')
  App.url_map.strict_slashes = False
  App.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )
  
  @App.route('/hello')
  def Hello():
    return 'Hello World'
  
  # Register Routes
  App.register_blueprint(Home)
  
  return App