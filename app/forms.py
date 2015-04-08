# from flask.ext.wtf import Form
from flask.ext.wtf import Form
from wtforms.fields import TextField, StringField, PasswordField, BooleanField
from wtforms import validators, ValidationError


class QuestionForm(Form):
    topic = StringField('Topic',
        validators=[validators.required(),
        validators.length(min=5, max=50)])

    text = StringField('Text',
        validators=[validators.required(),
        validators.length(min=15, max=255)])

class AnswerForm(Form):
    text = StringField('Text',
        validators=[validators.required(),
        validators.length(min=3, max=255)])