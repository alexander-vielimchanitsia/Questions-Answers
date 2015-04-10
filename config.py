import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True

SECRET_KEY = 'S5BvUsteq6ltYf05R32hfh2C29YE9W1L'

# SQLALCHEMY_DATABASE_URI = "postgresql://admin:admin@localhost/questions_answers_db"
if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') + '?check_same_thread=False'
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_RECORD_QUERIES = True
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

POSTS_PER_PAGE = 3