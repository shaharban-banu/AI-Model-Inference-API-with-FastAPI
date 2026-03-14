from database import Base
from sqlalchemy import Column,Integer,String

class User(Base):
    __tablename__='users'

    id=Column(Integer,primary_key=True)
    username=Column(String,unique=True)
    password=Column(String)

class Predictions(Base):
    __tablename__='predictions'

    id=Column(Integer,primary_key=True)
    user_id=Column(Integer)
    text=Column(String)
    result=Column(String)

