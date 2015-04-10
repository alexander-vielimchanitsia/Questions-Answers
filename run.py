#!../bin/python

# import os
# os.environ['DATABASE_URL'] = 'mysql://apps:apps@localhost/apps'

from app import app


app.run(debug = True)