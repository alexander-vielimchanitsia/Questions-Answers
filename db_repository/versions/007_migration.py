from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
question = Table('question', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('topic', VARCHAR(length=50)),
    Column('date', DATETIME),
    Column('text', VARCHAR(length=255)),
    Column('views', INTEGER),
)

question = Table('question', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=50)),
    Column('text', String(length=255)),
    Column('date', DateTime),
    Column('views', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['question'].columns['topic'].drop()
    post_meta.tables['question'].columns['title'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['question'].columns['topic'].create()
    post_meta.tables['question'].columns['title'].drop()
