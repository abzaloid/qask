from flask import Flask, render_template, request, redirect, url_for, flash, session

from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

from flask.ext.bcrypt import Bcrypt

from qask_database_setup import Base, Author, Comment, Question, Answer, Category

import time

engine = create_engine('sqlite:///qask.db')
Base.metadata.bind = engine

DBdb = sessionmaker(bind=engine)
db = DBdb()

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/')
def main():

	user = 0
	if "user" in session:
		user = db.query(Author).filter_by(login=session['user']).first()

	interesting = db.query(Category).filter_by(title='Interesting').one()
	interesting_questions = db.query(Question).filter_by(category_id=interesting.id).order_by(desc(Question.updated_time))
	interesting_answers = []
	interesting_comments = []
	for i in interesting_questions:
		interesting_answers.append(db.query(Answer).filter_by(question_id=i.id).count())
		interesting_comments.append(db.query(Comment).filter_by(question_id=i.id).count())
	
	general = db.query(Category).filter_by(title='General').one()
	general_questions = db.query(Question).filter_by(category_id=general.id).order_by(desc(Question.updated_time))
	general_answers = []
	general_comments = []
	for i in general_questions:
		general_answers.append(db.query(Answer).filter_by(question_id=i.id).count())
		general_comments.append(db.query(Comment).filter_by(question_id=i.id).count())
	
	academic = db.query(Category).filter_by(title='Academic').one()
	academic_questions = db.query(Question).filter_by(category_id=academic.id).order_by(desc(Question.updated_time))
	academic_answers = []
	academic_comments = []
	for i in academic_questions:
		academic_answers.append(db.query(Answer).filter_by(question_id=i.id).count())
		academic_comments.append(db.query(Comment).filter_by(question_id=i.id).count())


	return render_template('home.html', 
		interesting=interesting_questions, 
		interesting_answers=interesting_answers, 
		interesting_comments=interesting_comments,
		general=general_questions, 
		general_answers=general_answers, 
		general_comments=general_comments,
		academic=academic_questions, 
		academic_answers=academic_answers, 
		academic_comments=academic_comments,
		user = user)

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		register_name = request.form['register-name']
		register_login = request.form['register-login']
		register_email = request.form['register-email']
		register_password = request.form['register-password']
		register_password_repeat = request.form['register-password-repeat']

		if not register_name or not register_login or not register_email or not register_password or not register_password_repeat:
			flash("Please, fill all input forms", "error")
			return redirect(url_for('main'))

		if register_password != register_password_repeat:
			flash("Passwords do not match", "error")
			return redirect(url_for('main'))

		if db.query(Author).filter_by(login=register_login).count() > 0 or db.query(Author).filter_by(email=register_email).count() > 0:
			flash("The user with the same login or email already exists", "error")
			return redirect(url_for('main'))

		author = Author(email=register_email, 
			name=register_name,
			login=register_login,
			password_hash=bcrypt.generate_password_hash(register_password),
			added_time=time.time())

		db.add(author)
		db.commit()

		session['user'] = register_login

		flash("You are successfully registered and logged in!")

		return redirect(url_for('main'))
	else:
		return redirect(url_for('main'))

@app.route('/logout')
def logout():
	session.pop('user', None)
	return redirect(url_for('main'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		user_login = request.form['login-login']
		user_passw = request.form['login-password']

		if not user_login or not user_passw:
			flash("Please, fill all input forms","error")
			return redirect(url_for('main'))

		user = db.query(Author).filter_by(login=user_login)
		if user:
			user = user.first()
			if user and bcrypt.check_password_hash(user.password_hash, user_passw):
				print 'Yahoo'
				session['user'] = user_login
				flash("Login is successful","success")
				return redirect(url_for('main'))
			else:
				flash("Password or Login is incorrect","error")
				return redirect(url_for('main'))
		else:
			flash("Password or Login is incorrect","error")
			return redirect(url_for('main'))
	else:
		return redirect(url_for('main'))

@app.route('/question/<int:category_id>/<int:question_id>/')
def questionShow(category_id, question_id):

	user = 0
	if "user" in session:
		user = db.query(Author).filter_by(login=session['user']).first()


	question = db.query(Question).filter_by(id=question_id)

	if not question or question.count() == 0:
		flash("Wow, something wrong happened!!! Easy, man!", "error")
		return redirect(url_for('main'))

	question = question.one()

	answers = db.query(Answer).filter_by(question_id=question_id).order_by(desc(Answer.added_time))
	comments = db.query(Comment).filter_by(question_id=question_id).order_by(desc(Comment.added_time))

	return render_template('question.html', question=question, 
		answers=answers, 
		comments=comments, 
		alen=answers.count(), 
		clen=comments.count(),
		user=user)

@app.route('/answer/<int:category_id>/<int:question_id>/', methods=['GET', 'POST'])
def addAnswer(category_id, question_id):

	user = 0
	if "user" in session:
		user = db.query(Author).filter_by(login=session['user']).first()


	question = db.query(Question).filter_by(id=question_id)

	if not question or question.count() == 0:
		flash("Wow, something wrong happened!!! Easy, man!", "error")
		return redirect(url_for('main'))

	question = question.one()

	author = 0
	if 'user' in session:
		author = session['user']
		author = db.query(Author).filter_by(login=author).first()
	else:
		flash("Please, login!", "error")
		return redirect(url_for('questionShow', category_id=category_id, question_id=question_id))

	if request.method == 'POST':

		body = request.form['body']
		is_anonym = 1 if request.form.get('is_anonym') else 0

		answer = Answer(body=body,
			author=author,
			is_anonym=is_anonym,
			question=question,
			added_time=time.time()
			)

		db.add(answer)
		db.commit()

		flash("You have added new answer!", "success")

		return redirect(url_for('questionShow', category_id=category_id, question_id=question_id))
	else:
		
		answers = db.query(Answer).filter_by(question_id=question_id)
		comments = db.query(Comment).filter_by(question_id=question_id)

		return render_template('question.html', question=question, 
		answers=answers, 
		comments=comments, 
		alen=answers.count(), 
		clen=comments.count(),
		is_answering=1,
		user=user)

@app.route('/comment/<int:category_id>/<int:question_id>/', methods=['GET', 'POST'])
def addComment(category_id, question_id):

	user = 0
	if "user" in session:
		user = db.query(Author).filter_by(login=session['user']).first()


	question = db.query(Question).filter_by(id=question_id)

	if not question or question.count() == 0:
		flash("Wow, something wrong happened!!! Easy, man!", "error")
		return redirect(url_for('main'))

	question = question.one()

	author = 0
	if 'user' in session:
		author = session['user']
		author = db.query(Author).filter_by(login=author).first()
	else:
		flash("Please, login!", "error")
		return redirect(url_for('questionShow', category_id=category_id, question_id=question_id))

	if request.method == 'POST':

		body = request.form['body']
		is_anonym = 1 if request.form.get('is_anonym') else 0

		comment = Comment(body=body,
			author=author,
			is_anonym=is_anonym,
			question=question,
			added_time=time.time()
			)

		db.add(comment)
		db.commit()

		flash("You have added new comment!", "success")

		return redirect(url_for('questionShow', category_id=category_id, question_id=question_id))
	else:
		
		answers = db.query(Answer).filter_by(question_id=question_id)
		comments = db.query(Comment).filter_by(question_id=question_id)

		return render_template('question.html', question=question, 
		answers=answers, 
		comments=comments, 
		alen=answers.count(), 
		clen=comments.count(),
		is_commenting=1,
		user=user)

@app.route('/ask', methods=['POST'])
def askQuestion():
	user = 0
	if "user" in session:
		user = db.query(Author).filter_by(login=session['user']).first()

	title = request.form.get('title')
	body = request.form.get('body')
	category = request.form.get('category')
	is_anonym = 1 if request.form.get('is_anonym') else 0

	if not title or len(title) == 0 or not body or len(body) == 0 or not category or len(category) == 0:
		flash("Please fill all gaps", "error")
		return redirect(url_for('main'))

	print category
	category = db.query(Category).filter_by(title=category).first()

	question = Question(title=title, 
		body=body,
		added_time=time.time(),
		updated_time=time.time(),
		category=category,
		author=user,
		is_anonym=is_anonym)

	db.add(question)
	db.commit()

	flash("You have successfully asked a question", "successfully")

	return redirect(url_for('main'))

@app.route('/edit/<int:question_id>/', methods=['POST'])
def editQuestion(question_id):
	user = 0
	if "user" in session:
		user = db.query(Author).filter_by(login=session['user']).first()

	title = request.form.get('title')
	body = request.form.get('body')
	is_anonym = 1 if request.form.get('is_anonym') else 0

	if not title or len(title) == 0 or not body or len(body) == 0:
		flash("Please fill all gaps", "error")
		return redirect(url_for('main'))

	question = db.query(Question).filter_by(id=question_id).first()
	
	question.title = title
	question.body = body
	question.updated_time = time.time()
	question.is_anonym = is_anonym

	db.commit()

	flash("You have successfully edited a question", "successfully")

	return redirect(url_for('questionShow', category_id=question.category_id, question_id=question.id))

@app.route('/delete/<int:category_id>/<int:question_id>/', methods=["GET"])
def deleteQuestion(category_id, question_id):

	user = 0
	if "user" in session:
		user = db.query(Author).filter_by(login=session['user']).first()

	if user == 0:
		flash("Something wrong happened", "error")
		return redirect(url_for('main'))

	db.query(Question).filter_by(id=question_id).delete()

	flash("You have successfully deleted your question", "success")

	return redirect(url_for('main'))

if __name__ == "__main__":
	app.secret_key = 'my super secret fkey'
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)