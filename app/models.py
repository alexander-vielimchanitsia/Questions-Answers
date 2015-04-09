from app import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id',db.Integer , primary_key=True)
    username = db.Column('username', db.String(20), unique=True , index=True)
    password = db.Column('password' , db.String(10))
    email = db.Column('email',db.String(50),unique=True , index=True)
    registered_on = db.Column('registered_on' , db.DateTime)
 
    def __init__(self , username ,password , email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()
 
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return '<User %r>' % (self.username)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    text = db.Column(db.String(255))
    date = db.Column(db.DateTime)
    views = db.Column(db.Integer)
    answers = db.relationship('Answer', backref='question',
        lazy='dynamic')

    def __repr__(self):
        return '<Question %r>' % (self.title)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(255))
    date = db.Column(db.DateTime)
    rating = db.Column(db.Integer, default=0)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

    def __repr__(self):
        return '<Answer %r>' % (self.text)