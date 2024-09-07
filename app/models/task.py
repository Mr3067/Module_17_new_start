from app.backend.db import Base
from sqlalchemy import Column, String, Integer, Float, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app.models.user import User


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title  = Column(String)
    content  = Column(String)
    priority  = Column(Integer, default=0)
    completed  = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable= True, index=True)
    slug = Column(String, unique=True, index=True)
    usrer = relationship("User", back_populates='tasks')


from sqlalchemy.schema import CreateTable

a = CreateTable(Task.__table__)
print(a)