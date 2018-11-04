#!/usr/bin/python
'''
author: Tobias Weis
'''

import multiprocessing
import time
import datetime

class Runner(multiprocessing.Process):
    def __init__(self, config, md, alarms, models):
        multiprocessing.Process.__init__(self)
        self.config = config
        self.md = md
        self.models = models

        self.alarms = alarms

        print "[Runner] got the following alarms:"
        for a in self.alarms:
            print a
            print dir(a)
        print "[Runner] ----------------"

    def run(self):
        while not self.md["shutdown"]:
            self.run_impl()

        self.cleanup()

    def run_impl(self):
        time.sleep(10)
        if self.md["update_alarms"]:
            self.alarms = self.models.Alarm.query.all()
            self.md["update_alarms"] = False
            print "[Runner] - updated alarms"

        # TODO: implement day-check
        for a in self.alarms:
            now = datetime.datetime.now()
            print "Alarmtime: %d:%d" % (a.hour, a.minute)
            print "Nowtime: %d:%d" % (now.hour, now.minute)
            if a.hour == now.hour and a.minute == now.minute:
                print "ALARM - ALARM - ALARM - ALARM"


        print "[Runner]."

    def cleanup(self):
        print "Runner cleaning up"

