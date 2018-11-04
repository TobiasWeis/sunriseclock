from flask import Flask
import os
#from models import *

app = Flask(__name__)
app.jinja_env.cache = {}
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CACHE_TYPE'] = "null"
app.secret_key = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'



from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

from app import views, models

# initially create database if it does not exit
if not os.path.isfile(app.config['SQLALCHEMY_DATABASE_URI']):
    # check if tables are empty
    try:
        models.Sound.query.all()
    except:
        print "Creating database"
        db.create_all()
        # add sample alarm
        s = models.Sound("First sound", "/tmp/test.mp3")
        db.session.add(s)
        st = models.Sunrisetype("Normal")
        db.session.add(st)
        sa = models.Alarm("SampleAlarm", 9, 0, -1, 30, 0, 0)
        db.session.add(sa)
        db.session.commit()


