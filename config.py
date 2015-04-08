import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True

SECRET_KEY = 'S5BvUsteq6ltYf05R32hfh2C29YE9W1L'

# SQLALCHEMY_DATABASE_URI = "postgresql://admin:admin@localhost/questions_answers_db"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')