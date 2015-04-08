from app import app, db
from flask import render_template, flash, redirect, request, url_for
import datetime

from models import Question, Answer
from forms import QuestionForm, AnswerForm


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