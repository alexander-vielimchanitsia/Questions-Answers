from app import app, db
from flask import render_template, flash, redirect, request, url_for, session
from flask.ext.login import login_user, logout_user, current_user, login_required
import datetime

from models import Question, Answer, User
from forms import QuestionForm, AnswerForm, LoginForm, RegistrationForm


@app.route('/')
def index():
    questions = Question.query.all()
    return render_template('index.html',
        questions = questions)

@app.route('/question/add', methods=['GET', 'POST'])
def question_add():
    if request.method == 'POST':
        form = QuestionForm(request.form)

        question = Question(
            # request.form['topic'],
            # request.form['text'])
            topic = request.form['topic'],
            text = request.form['text'],
            date = datetime.datetime.now())

        db.session.add(question)
        db.session.commit()

        # if form.validate_on_submit():
        return redirect(url_for('index'))
    else:
        print 'Error'
        form = QuestionForm()

    return render_template('question_add.html', form = form)

@app.route('/question/<id>/review', methods=['GET', 'POST'])
def question_review(id):
    question = Question.query.get_or_404(id)
    answers = Answer.query.filter_by(question_id=id)

    if request.method == 'POST':
        form = AnswerForm(request.form)

        answer = Answer(
            text = request.form['text'],
            date = datetime.datetime.now(),
            question_id = id)

        db.session.add(answer)
        db.session.commit()
        # return redirect('/question/' + id + '/review')
        return redirect(url_for('question_review', id=id))
    else:
        form = AnswerForm()

    return render_template('question_review.html',
        question = question,
        answers = answers)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        username = request.form['username']
        password = request.form['password']
        registered_user = User(username=username,password=password)
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
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))