from backend import db
from sqlalchemy import Column, String, Integer, Float, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
# from models.task import Task - включишь это и работать не будет


class User(db.Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship("Task", back_populates='user') #!!!!!

from sqlalchemy.schema import CreateTable

a = CreateTable(User.__table__)
print(a)
