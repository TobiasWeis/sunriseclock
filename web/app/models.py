try:
    from app import db
except:
    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy()

class Alarm(db.Model):
    def __init__(self, name, hour, minute, weekdays, duration, sunrise_id, sound_id):
        self.name = name
        self.hour = hour
        self.minute = minute
        self.weekdays = weekdays
        self.duration = duration
        self.sunrise_id = sunrise_id
        self.sound_id = sound_id

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR)
    hour = db.Column(db.Integer)
    minute = db.Column(db.Integer)
    weekdays = db.Column(db.VARCHAR)
    duration = db.Column(db.Integer)
    sunrise_id = db.Column(db.Integer, db.ForeignKey('sunrisetype.id'))
    sound_id = db.Column(db.Integer, db.ForeignKey('sound.id'))

    def __repr__(self):
        return '<Alarm %r (%s): %02d:%02d>' % (self.id, self.name, self.hour, self.minute)
        return '<Alarm %r>' % self.id

class Sound(db.Model):
    def __init__(self, name, filename):
        self.name = name
        self.filename = filename

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR)
    filename = db.Column(db.VARCHAR)

class Sunrisetype(db.Model):
    def __init__(self, name):
        self.name = name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR)
