# -*- coding: utf-8 -*-

from app import app, db, login_manager
from flask import render_template, flash, redirect, request, url_for, session
from flask.ext.login import login_user, logout_user, current_user, login_required
from datetime import datetime
import hashlib

from config import POSTS_PER_PAGE

from models import Question, Answer, User
from forms import QuestionForm, AnswerForm, LoginForm, RegistrationForm


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

# flash_errors for show all errors in a forms
def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index/page/<int:page>', methods=['GET', 'POST'])
def index(page=1):
    questions = Question.query.paginate(page, POSTS_PER_PAGE, False)
    return render_template('index.html',
        questions = questions)

@app.route('/question/add', methods=['GET', 'POST'])
def question_add():
    # was form posted?
    if request.method == 'POST':
        form = QuestionForm(request.form)
        if form.validate_on_submit():

            question = Question(
                title = request.form['title'],
                text = request.form['text'],
                date = datetime.now())

            # Answer save in db
            db.session.add(question)
            db.session.commit()

            return redirect(url_for('index'))

        else:
            # Show errors in form
            flash_errors(form)

    else:
        form = QuestionForm()

    return render_template('question_add.html', form=form)

@app.route('/question/<id>/review', methods=['GET', 'POST'])
def question_review(id):
    # Get the question
    question = Question.query.get_or_404(id)

    # All answers in this question
    answers = Answer.query.filter_by(question_id=id)

    # was form posted?
    if request.method == 'POST':
        form = AnswerForm(request.form)

        if form.validate_on_submit():
            answer = Answer(
                text = request.form['text'],
                date = datetime.now(),
                question_id = id)

            # Answer save in db
            db.session.add(answer)
            db.session.commit()

            return redirect(url_for('question_review', id=id))

        else:
            # Show errors in form
            flash_errors(form)

    else:
        form = AnswerForm()

    return render_template('question_review.html',
        form = form,
        question = question,
        answers = answers)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        registered_user = User.query.filter_by(username=username,password=password).first()

        if registered_user is None:
            flash('Username or Password is invalid' , 'error')
            # return redirect(url_for('login'))

        login_user(registered_user)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("index"))
    return render_template("login.html", form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(form.username.data, form.password.data,
                        form.email.data)
            db.session.add(user)
            db.session.commit()
            flash('Thanks for registering')
            return redirect(url_for('login'))
        else:
            flash_errors(form)
    return render_template('register.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/question/<id>/review/like/<answer_id>', methods=['GET', 'POST'])
def like(id, answer_id):
    answer = Answer.query.get(answer_id)
    answer.rating += 1
    db.session.commit()

    return redirect(url_for('question_review', id=id))

@app.route('/question/<id>/review/dislike/<answer_id>', methods=['GET', 'POST'])
def dislike(id, answer_id):
    answer = Answer.query.get(answer_id)
    answer.rating -= 1
    db.session.commit()

    return redirect(url_for('question_review', id=id))