from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
users = Table('users', post_meta,
    Column('user_id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=20)),
    Column('password', String(length=10)),
    Column('email', String(length=50)),
    Column('registered_on', DateTime),
)

question = Table('question', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('topic', VARCHAR(length=50)),
    Column('description', VARCHAR(length=255)),
    Column('date', DATETIME),
)

question = Table('question', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('topic', String(length=50)),
    Column('text', String(length=255)),
    Column('date', DateTime),
    Column('views', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['users'].create()
    pre_meta.tables['question'].columns['description'].drop()
    post_meta.tables['question'].columns['text'].create()
    post_meta.tables['question'].columns['views'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['users'].drop()
    pre_meta.tables['question'].columns['description'].create()
    post_meta.tables['question'].columns['text'].drop()
    post_meta.tables['question'].columns['views'].drop()
