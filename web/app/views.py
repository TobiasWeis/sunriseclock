from app import app
from app import config,db,models,md
from flask import render_template, redirect, url_for, send_file, request, flash, jsonify
from sqlalchemy.sql.expression import func
import json

@app.route('/')
def index():
    """
    Serve the website
    """
    alarms = models.Alarm.query.all()
    sounds = models.Sound.query.all()
    sunrises = models.Sunrisetype.query.all()

    print "[views.py]: ", alarms

    return render_template('index.html', title='Home', alarms=alarms, sounds=sounds, sunrises=sunrises)

@app.route('/updatealarm', methods=['POST'])
def updatealarm():
    """
    Update alarm characteristics
    """
    print "[views.py] Received update to alarm:"
    print request.form
    print "[views.py] -----"

    try:
        a = models.Alarm.query.filter_by(id=request.form['id']).first()
        a.name = request.form["name"]
        a.hour = request.form["timetext"].split(":")[0]
        a.minute = request.form["timetext"].split(":")[1]
        # TODO
        #a.weekdays = ...
        a.duration = request.form["duration"]
        a.sunrise_id = request.form["sunrise_id"]
        a.sound_id = request.form["sound_id"]

        db.session.commit()

        # now we need to update the runner's alarms
        md["alarms"] = models.Alarm.query.all()
        md["update_alarms"] = True
    except Exception, e:
        print "EXCEPTION: ", e
        return json.dumps({'status':'FAIL'})

    return json.dumps({'status':'OK'})

@app.route('/deletealarm', methods=['Post'])
def deletealarm():
    """
    delete alarm completely from database
    """
    try:
        delid = request.form["id"]
        a = models.Alarm.query.filter_by(id=delid).first()
        db.session.delete(a)
        db.session.commit()
    except Exception, e:
        print "[views.py] EXCEPTION: ", e
        return json.dumps({'status':'FAIL'})

    return json.dumps({'status':'OK'})


@app.route('/createalarm', methods=['POST'])
def createalarm():
    """
    create a NEW alarm
    """
    try:
        name = request.form["name"]
        hour = request.form["timetext"].split(":")[0]
        minute = request.form["timetext"].split(":")[1]
        # TODO
        #a.weekdays = ...
        duration = request.form["duration"]
        sunrise_id = request.form["sunrise_id"]
        sound_id = request.form["sound_id"]

        a = models.Alarm(
                name=name,
                hour=hour,
                minute=minute,
                weekdays=-1,
                duration=duration,
                sunrise_id=sunrise_id,
                sound_id=sound_id
                        )

        db.session.add(a)
        db.session.commit()

        # now we need to update the runner's alarms
        md["alarms"] = models.Alarm.query.all()
        md["update_alarms"] = True
    except Exception, e:
        print "EXCEPTION: ", e
        return json.dumps({'status':'FAIL'})

    return json.dumps({'status':'OK'})

