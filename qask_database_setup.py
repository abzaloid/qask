import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)


class Author (Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    login = Column(String(30), nullable=False)
    password_hash = Column(String(250), nullable=False)
    added_time = Column(Float)


class Question(Base):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    body = Column(String(1000), nullable=False)
    added_time = Column(Float)
    updated_time = Column(Float)
    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship(Author)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    is_anonym = Column(Integer)


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    body = Column(String(500), nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship(Author)
    question_id = Column(Integer, ForeignKey('question.id'))
    question = relationship(Question)
    is_anonym = Column(Integer)
    added_time = Column(Float)

class Answer(Base):
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=True)
    body = Column(String(500), nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship(Author)
    question_id = Column(Integer, ForeignKey('question.id'))
    question = relationship(Question)
    is_anonym = Column(Integer)
    added_time = Column(Float)

engine = create_engine('sqlite:///qask.db')


Base.metadata.create_all(engine)