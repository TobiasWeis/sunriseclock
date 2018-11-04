from app import app
from app import config,db,models
from flask import render_template, redirect, url_for, send_file, request, flash, jsonify
from sqlalchemy.sql.expression import func
import json

@app.route('/')
def index():
    """
    Serve the website
    """
    alarms = models.Alarm.query.all()

    print alarms

    return render_template('index.html', title='Home', alarms=alarms)

@app.route('/savetime', methods=['POST'])
def savetime():
    """
    Receive newly set time

    TODO: save to database
    """
    time = request.form['timetext']
    print "Got time: ", time
    return json.dumps({'status':'OK'})

