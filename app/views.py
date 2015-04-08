from app import app, db
from flask import render_template, flash, redirect, request
import datetime

from models import Question, Answer
from forms import QuestionForm, AnswerForm


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/question/add', methods=['GET', 'POST'])
def question_add():
    if request.method == 'POST':
        form = QuestionForm(request.form)

        question = Question(
            # request.form['topic'],
            # request.form['text'])
            topic = request.form['topic'],
            text = request.form['topic'],
            date = datetime.datetime.now())

        db.session.add(question)
        db.session.commit()

        print Question.query.get(2).date
        # if form.validate_on_submit():
        return redirect('/')
        print 'Yessss'
    else:
        print 'Error'
        form = QuestionForm()
    #     return redirect('/')
    return render_template('question_add.html', form = form)

@app.route('/question/review')
def question_review():
    return render_template('question_review.html')