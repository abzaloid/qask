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

# adding fake users

abz = Author(name="Abzal Serekov", 
       email="abzal.serekov@gmail.com", 
       login="abz", 
       password_hash=bcrypt.generate_password_hash('hello'), 
       added_time=time.time(),)
session.add(abz)
session.commit()
admin = Author(name="Admin Admin", 
       email="admin@qask.kz", 
       login="admin", 
       password_hash=bcrypt.generate_password_hash('admin'), 
       added_time=time.time(),)
session.add(admin)
session.commit()
test = Author(name="Test Testoff", 
       email="test@gmail.com", 
       login="test", 
       password_hash=bcrypt.generate_password_hash('test'), 
       added_time=time.time(),)
session.add(test)
session.commit()

# adding fake categories

interesting = Category(title="Interesting", description="Here you can find the most interesting questions and answers with comments!")
session.add(interesting)
session.commit()
general = Category(title="General", description="Here you can find general-type questions")
session.add(general)
session.commit()
academic = Category(title="Academic", description="Here you can find academic questions")
session.add(academic)
session.commit()

# adding fake questions

question1 = Question(title="What invention by Garnet Carter made",
       body="What invention by Garnet Carter made its debut at the Fairyland Inn Resort in Lookout Mountain, Tennessee, in 1927?",
       added_time=time.time(),
       updated_time=time.time(),
       author=abz,
       category=interesting,
       is_anonym=0)
session.add(question1)
session.commit()

question2 = Question(title="Who invented the phonograph?",
       body="Who invented the phonograph?",
       added_time=time.time(),
       updated_time=time.time(),
       author=abz,
       category=academic,
       is_anonym=1)
session.add(question2)
session.commit()

question3 = Question(title="This African-American woman physical therapist ",
       body="This African-American woman physical therapist worked with soldiers disabled in World War II. She invented a device that helped the disabled to eat by delivering food through a tube to a mouthpiece.",
       added_time=time.time(),
       updated_time=time.time(),
       author=admin,
       category=general,
       is_anonym=0)
session.add(question3)
session.commit()


question4 = Question(title="What toy was invented by Joshua Lionel Cowen around 1900?",
       body="What toy was invented by Joshua Lionel Cowen around 1900?",
       added_time=time.time(),
       updated_time=time.time(),
       author=test,
       category=interesting,
       is_anonym=0)
session.add(question4)
session.commit()

question5 = Question(title="For whom high heeled shoes were invented?",
       body="For whom high heeled shoes were invented?",
       added_time=time.time(),
       updated_time=time.time(),
       author=test,
       category=general,
       is_anonym=0)
session.add(question5)
session.commit()

question6 = Question(title="What toy did George Lerner create for Hasbro company in 1952?",
       body="What toy did George Lerner create for Hasbro company in 1952?",
       added_time=time.time(),
       updated_time=time.time(),
       author=admin,
       category=general,
       is_anonym=1)
session.add(question6)
session.commit()

question7 = Question(title="Who invented Dynamite?",
       body="Who invented Dynamite?",
       added_time=time.time(),
       updated_time=time.time(),
       author=test,
       category=academic,
       is_anonym=0)
session.add(question7)
session.commit()

question8 = Question(title="Who came up with the idea for INSTANT MASHED POTATO?",
       body="Who came up with the idea for INSTANT MASHED POTATO?",
       added_time=time.time(),
       updated_time=time.time(),
       author=admin,
       category=interesting,
       is_anonym=0)
session.add(question8)
session.commit()

question9 = Question(title="William Frederick is credited with the invention...",
       body="William Frederick is credited with the invention of the modern frisbee in the mid 1950's. In 1957 the Wham-O Company bought his idea and the rest is history. They named the toy after William Frisbie who was a ________?",
       added_time=time.time(),
       updated_time=time.time(),
       author=abz,
       category=general,
       is_anonym=0)
session.add(question9)
session.commit()


question10 = Question(title="Who developed the idea of Crop Rotation?",
       body="Who developed the idea of Crop Rotation?",
       added_time=time.time(),
       updated_time=time.time(),
       author=test,
       category=academic,
       is_anonym=0)
session.add(question10)
session.commit()

question11 = Question(title="For over 500 years, paper was",
       body="For over 500 years, paper was only available and sold as single sheets. In 1902, an inventive Australian used half size sheets of paper, a bit of glue and cardboard to create the what?",
       added_time=time.time(),
       updated_time=time.time(),
       author=admin,
       category=academic,
       is_anonym=0)
session.add(question11)
session.commit()

question12 = Question(title="This statesman, politican, scholar, inventor",
       body="This statesman, politican, scholar, inventor, and one of early presidents of USA invented the swivel chair, the spherical sundial, the moldboard plow, and the cipher wheel.",
       added_time=time.time(),
       updated_time=time.time(),
       author=admin,
       category=interesting,
       is_anonym=0)
session.add(question12)
session.commit()


question13 = Question(title="What is the name of the CalTech ",
       body="What is the name of the CalTech seismologist who invented the scale used to measure the magnitude of earthquakes?",
       added_time=time.time(),
       updated_time=time.time(),
       author=abz,
       category=academic,
       is_anonym=1)
session.add(question13)
session.commit()

question14 = Question(title="Which scientist discovered the radioactive element radium?",
       body="Which scientist discovered the radioactive element radium?",
       added_time=time.time(),
       updated_time=time.time(),
       author=test,
       category=general,
       is_anonym=0)
session.add(question14)
session.commit()

question15 = Question(title="What J. B. Dunlop invented?",
       body="What J. B. Dunlop invented?",
       added_time=time.time(),
       updated_time=time.time(),
       author=admin,
       category=interesting,
       is_anonym=0)
session.add(question15)
session.commit()

question16 = Question(title="In which decade was the first solid state integrated circuit demonstrated?",
       body="In which decade was the first solid state integrated circuit demonstrated?",
       added_time=time.time(),
       updated_time=time.time(),
       author=abz,
       category=interesting,
       is_anonym=1)
session.add(question16)
session.commit()

question17 = Question(title="Who invented the BALLPOINT PEN?",
       body="Who invented the BALLPOINT PEN?",
       added_time=time.time(),
       updated_time=time.time(),
       author=abz,
       category=academic,
       is_anonym=1)
session.add(question17)
session.commit()

question18 = Question(title="This is a fake question?",
       body="Lorem ipsum and blablabla Lorem ipsum and blablabla Lorem ipsum and blablabla",
       added_time=time.time(),
       updated_time=time.time(),
       author=admin,
       category=academic,
       is_anonym=0)
session.add(question18)
session.commit()


question19 = Question(title="How can I deal with 'difficult' people?",
       body="Hi,<br/>What is the way to deal with really stupid difficult people?<br/>Thanks",
       added_time=time.time(),
       updated_time=time.time(),
       author=abz,
       category=interesting,
       is_anonym=1)
session.add(question19)
session.commit()

question20 = Question(title="Is there any way to solve inverse kinematics in linear time?",
       body="Dear all,<br/>I know that there exist a lot of different iterative methods to solve inverse kinematics problem for N-DoF system, however I need the linear one which runs in O(N).<br/>Does anybody know is there any way to make it?<br/>Thanks",
       added_time=time.time(),
       updated_time=time.time(),
       author=admin,
       category=academic,
       is_anonym=0)
session.add(question20)
session.commit()


question21 = Question(title="How can I hack this site?",
       body="Hi there,<br/>Is there any way I can hack this site?<br/>Thanks,",
       added_time=time.time(),
       updated_time=time.time(),
       author=test,
       category=interesting,
       is_anonym=1)
session.add(question21)
session.commit()
comment21_1 = Comment(body="Well, well, well.... Oh, by the way, I am the admin :)", author=admin, question=question21, is_anonym=0, added_time=time.time())
session.add(comment21_1)
session.commit()


question22 = Question(title="How to solve x^2=100",
       body="Please, help!<br/>I can't solve this equation x^2=100, where x in R<br/>Thanks",
       added_time=time.time(),
       updated_time=time.time(),
       author=abz,
       category=academic,
       is_anonym=1)
session.add(question22)
session.commit()
answer22_1 = Answer(body="I would suggest to learn bit of algebra for dummies<br/>x^2=100 => x=sqrt(100)=10", author=admin, question=question22, is_anonym=0, added_time=time.time())
session.add(answer22_1)
session.commit()

question23 = Question(title="What is the shortest path to university?",
       body="Dear all:<br/>What is the shortest route to the university?<br/>Thanks,Anonym",
       added_time=time.time(),
       updated_time=time.time(),
       author=admin,
       category=general,
       is_anonym=1)
session.add(question23)
session.commit()
answer23_1 = Answer(body="Hello, 2gis will be very helpful for you!", author=abz, question=question23, is_anonym=0, added_time=time.time())
session.add(answer23_1)
session.commit()
comment23_1 = Comment(body="What do you mean by 'shortest'?", author=test, question=question23, is_anonym=0, added_time=time.time())
session.add(comment23_1)
session.commit()

question24 = Question(title="Who am I?",
       body="Dear all: <br/>How can I know what is my name?",
       added_time=time.time(),
       updated_time=time.time(),
       author=abz,
       category=general,
       is_anonym=1)
session.add(question24)
session.commit()
answer24_1 = Answer(body="Ok, just .. off", author=abz, question=question24, is_anonym=1, added_time=time.time())
session.add(answer24_1)
session.commit()

question25 = Question(title="What is the color of the Sun?",
       body="I am wondering what is the color of the Sun, huh?",
       added_time=time.time(),
       updated_time=time.time(),
       author=admin,
       category=interesting,
       is_anonym=0)
session.add(question25)
session.commit()
comment25_1 = Comment(body="What? Again some sarcasm?", author=abz, question=question25, is_anonym=0, added_time=time.time())
comment25_2 = Comment(body="No, I really don't know!", author=admin, question=question25, is_anonym=0, added_time=time.time())
comment25_3 = Comment(body="Maaan....", author=test, question=question25, is_anonym=1, added_time=time.time())
session.add(comment25_1)
session.commit()
session.add(comment25_2)
session.commit()
session.add(comment25_3)
session.commit()
answer25_1 = Answer(body="Yellow", author=abz, question=question25, is_anonym=0, added_time=time.time())
answer25_2 = Answer(body="<sarcasm>White.....)))</sarcasm>", author=abz, question=question25, is_anonym=1, added_time=time.time())
session.add(answer25_1)
session.commit()
session.add(answer25_2)
session.commit()

print "added all fake items!"