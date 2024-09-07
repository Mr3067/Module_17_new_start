from sqlalchemy.orm import sessionmaker,DeclarativeBase
from sqlalchemy import create_engine

engine = create_engine('sqlite:///taskmanager.db', echo=True)

SessionLocal = sessionmaker(bind=engine) #сессия связи с базой данных; bind - параметр привязки

class Base(DeclarativeBase): # определение базового класса
    pass