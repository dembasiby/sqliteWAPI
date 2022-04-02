from sqlalchemy import (
    create_engine, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///mydb.db', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    full_name = Column(String)





class Car:
    pass