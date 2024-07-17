from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

load_dotenv()

# Connect To Database Using Environment Variables
Engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=Engine)
Base = declarative_base()

# NOTES:
#
# Engine variable manages the overall database connection.
# Session variable generates temporary connections for performing CRUD operations.
# Base class variable helps map the models to real MySQL tables.

# Set Up Database Connection In Flask App
def Init_Database(App):
  Base.metadata.create_all(Engine)
  
  # Run `Close_Database()` Whenever A Context Is Destroyed
  App.teardown_appcontext(Close_Database)
  
# Return A New Session-Connection Object
def Get_Database():
  if 'Database' not in g:
    # Save Current Connection On `g` Object (Store Database Connection In App Context)
    g.Database = Session()
  
  # Return Connection From `g` Object Instead Of Creating A New `Session` Instance Each Time
  return g.Database

# Leverage App Context To Close Connection When Request Officially Terminates
def Close_Database(e=None):
  # `pop()` Method Attempt To Find & Remove `Database` From `g` Object
  Database = g.pop('Database', None)
  
  # If Database Exists, End Connection
  if Database is not None:
    Database.close()