from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:1234@localhost:3306/todolist')

Session = sessionmaker(bind=engine)

Base = declarative_base()