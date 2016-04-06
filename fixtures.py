from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from qask_database_setup import Base, Author, Comment, Question, Answer, Category

import time

from flask import Flask
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

engine = create_engine('sqlite:///qask.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# These are fake examples of how we can insert data to our database 
# programmatically

# adding fake users

user = Author(name="Halit Enes", 
       email="halit@gmail.com", 
       login="halit", 
       password_hash=bcrypt.generate_password_hash('test'), 
       added_time=time.time(),)
session.add(user)
session.commit()

# adding fake categories

interesting = Category(title="Interesting", 
       description="fake description!")
session.add(interesting)
session.commit()

general = Category(title="General", description="blablabla")
session.add(general)
session.commit()

academic = Category(title="Academic", description="bla")
session.add(academic)
session.commit()

# adding fake questions

question1 = Question(title="What invention by Garnet Carter made",
       body="What invention by Garnet Carter made its debut at the Fairyland Inn Resort in Lookout Mountain, Tennessee, in 1927?",
       added_time=time.time(),
       updated_time=time.time(),
       author=user,
       category=interesting,
       is_anonym=0)
session.add(question1)
session.commit()

question2 = Question(title="Test Question?",
       body="Just another random question?",
       added_time=time.time(),
       updated_time=time.time(),
       author=user,
       category=general,
       is_anonym=0)
session.add(question2)
session.commit()

question3 = Question(title="Test Question 2?",
       body="Just another random question 2?",
       added_time=time.time(),
       updated_time=time.time(),
       author=user,
       category=academic,
       is_anonym=1)
session.add(question3)
session.commit()


print "added all fake items!"