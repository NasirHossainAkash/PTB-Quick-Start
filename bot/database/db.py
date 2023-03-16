from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('database://user:password@host:port/database_name')


Session = sessionmaker(bind=engine)


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


    def __init__(self,name,email):
        self.name = name
        self.email = email


Base.metadata.create_all(engine)
session = Session()
