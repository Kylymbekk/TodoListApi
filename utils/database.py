import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = sqlalchemy.create_engine("postgresql://abcde:postgres@localhost:5432/todolist")
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
Base = declarative_base()
