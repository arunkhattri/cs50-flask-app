# -*- coding=utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

engine = create_engine("postgres://gfmkzmyxtwcggf:0cee6a4bcf4167ea61a5c9dfe8e7b0f1904a0bfc7d57eb5fd45e80f292c7e80b@ec2-50-17-231-192.compute-1.amazonaws.com:5432/d2s3tb1rjh5m98")
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    isbn = Column(String(10))
    title = Column(String(100))
    author = Column(String)
    year = Column(Integer)

    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year


