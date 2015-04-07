from app import app
from flask import render_template, flash, redirect

from forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/question/add')
def question_add():
    return render_template('question_add.html')

@app.route('/question/review')
def question_review():
    return render_template('question_review.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
        title = 'Sign In',
        form = form)