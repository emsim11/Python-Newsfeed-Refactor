from App.Database import Base
from sqlalchemy import Column, Integer, ForeignKey

# No Unique Info Stored In This Model
# `Vote` Requires Reference To: Post Being Upvoted & Id Of Person Who Upvoted It
class Vote(Base):
  __tablename__ = 'Votes'
  Id = Column(Integer, primary_key=True)
  User_Id = Column(Integer, ForeignKey('Users.Id'))
  Post_Id = Column(Integer, ForeignKey('Posts.Id'))