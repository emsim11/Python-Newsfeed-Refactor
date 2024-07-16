from App.Database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt # Directly Use bcrypt Module

# Generate Salt Value Used In Hashing Password
Salt = bcrypt.gensalt()

# Define The Class
class User(Base):
  __tablename__ = 'Users'
  Id = Column(Integer, primary_key=True)
  Username = Column(String(50), nullable=False)
  Email = Column(String(50), nullable=False, unique=True)
  Password = Column(String(100), nullable=False)
    
  # Email Validation
  @validates('Email')
  def Validate_Email(Self, Key, Email):
    
    # Require Email Address To Contain @ Character
    assert '@' in Email
    return Email
    
  # Password Validation
  @validates('Password')
  def Validate_Password(Self, Key, Password):
      
    # Require Password To Be 8+ Characters
    assert len(Password) > 8
    
    # Return Encrypt Version Of Password
    return bcrypt.hashpw(Password.encode('utf-8'), Salt)