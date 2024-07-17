from App.Database import Base
from App.Models.Vote import Vote
from sqlalchemy import select, func, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, column_property
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
  
  # Define Post Model Relationship To `Comments` Table
  # Cascade Deletes Corresponding Foreign Key Records When A Record From Specified Table Is Deleted
  Comment = relationship('Comment', cascade='all,delete')
  
  # Define Dynamic Property For `Votes`` On Post Model
  # Query For A `Post` Returns Info About Number Of Votes Post Has
  # Cascade Deletes Every Vote Associated With A Post When Post Is Deleted
  Vote_Count = column_property(select(func.count(Vote.Id)).where(Vote.Post_Id == Id))
  Votes = relationship('Vote', cascade='all,delete')