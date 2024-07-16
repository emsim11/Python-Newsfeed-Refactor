from App.Database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime # Built-In Module To Generate Timestamps

# Define The Class
class Post(Base):
  __tablename__ = 'Posts'
  Id = Column(Integer, primary_key=True)
  Title = Column(String(100), nullable=False)
  Post_URL = Column(String(100), nullable=False)
  Created_At = Column(DateTime, default=datetime.now)
  Updated_At = Column(DateTime, default=datetime.now, onupdate=datetime.now)
  
  # Define ForeignKey That References `Users` Table
  User_Id = Column(Integer, ForeignKey('Users.Id'))
  User = relationship('User')