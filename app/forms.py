# from flask.ext.wtf import Form
from flask.ext.wtf import Form
from wtforms.fields import TextField, StringField, PasswordField, BooleanField
from wtforms import validators, ValidationError

from models import User


class QuestionForm(Form):
    title = StringField('Title',
        validators=[validators.Required(),
        validators.length(min=5, max=50)])

    text = StringField('Text',
        validators=[validators.Required(),
        validators.length(min=15, max=500)])

class AnswerForm(Form):
    text = StringField('Text',
        validators=[validators.Required(),
        validators.length(min=3, max=500)])

class LoginForm(Form):
    username = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(
            username=self.username.data).first()
        if user is None:
            self.username.errors.append('Unknown username')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])