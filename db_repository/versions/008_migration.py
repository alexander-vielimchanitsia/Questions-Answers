from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
answer = Table('answer', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('text', String(length=255)),
    Column('date', DateTime),
    Column('rating', Integer, default=ColumnDefault(0)),
    Column('question_id', Integer),
    Column('user_id', Integer),
)

question = Table('question', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=50)),
    Column('text', String(length=255)),
    Column('date', DateTime),
    Column('views', Integer),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['answer'].columns['user_id'].create()
    post_meta.tables['question'].columns['user_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['answer'].columns['user_id'].drop()
    post_meta.tables['question'].columns['user_id'].drop()
