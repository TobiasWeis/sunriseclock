from flask import Flask
import os
from multiprocessing import Process, Manager
from Runner import *

Manager = Manager()
md = Manager.dict()
md['shutdown'] = False
md['update_alarms'] = False

#from models import *

app = Flask(__name__)
app.jinja_env.cache = {}
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CACHE_TYPE'] = "null"
app.secret_key = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
app.md = md

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

from app import views, models

# initially create database if it does not exit
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
    sa = models.Alarm("SampleAlarm", hour=9, minute=0, weekdays=-1, duration=30, sunrise_id=0, sound_id=0)
    db.session.add(sa)
    db.session.commit()


# start the background-runner that will handle the alarms
runner = Runner(app.config, md, models.Alarm.query.all(), models)
runner.start()
