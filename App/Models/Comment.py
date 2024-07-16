from App.Database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime # Built-In Module To Generate Timestamps

class Comment(Base):
  __tablename__ = 'Comments'
  Id = Column(Integer, primary_key=True)
  Comment_Text = Column(String(255), nullable=False)
  Post_Id = Column(Integer, ForeignKey('Posts.Id'))
  Created_At = Column(DateTime, default=datetime.now)
  Updated_At = Column(DateTime, default=datetime.now, onupdate=datetime.now)
  
  # Define ForeignKey That References `Users` Table
  User_Id = Column(Integer, ForeignKey('Users.Id'))
  User = relationship('User')