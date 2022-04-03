from sqlalchemy import (
    create_engine, Column, Integer, String, Float)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from helpers import process_for_db

engine = create_engine('sqlite:///mydb.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    full_name = Column(String)

    def __repr__(self):
        return f'User <name: {self.name}'


class Agent(Base):
    __tablename__ = 'agents'

    id = Column(Integer, primary_key=True, autoincrement=True)
    age = Column(Integer)
    gender = Column(String)
    miles = Column(Float)
    debt = Column(Integer)
    income = Column(Integer)
    sales = Column(Integer)

    def __repr__(self):
        return f'Agent <age: {self.age}, gender: {self.gender}, sales: {self.sales}'


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    for agent in process_for_db('data/cars.csv'):
        _agent = Agent(age=agent['age'], gender=agent['gender'], miles=agent['miles'],
                       debt=agent['debt'], income=agent['income'], sales=agent['sales'])
        session.add(_agent)
        session.commit()
