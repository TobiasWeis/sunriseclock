#!/usr/bin/python
'''
author: Tobias Weis
'''

import multiprocessing
import time
import datetime
from pygame import mixer

class Runner(multiprocessing.Process):
    def __init__(self, config, md, alarms, models,db):
        multiprocessing.Process.__init__(self)
        self.config = config
        self.md = md
        self.models = models
        self.db = db

        self.alarms = alarms

        print "[Runner] got the following alarms:"
        for a in self.alarms:
            print a
        print "[Runner] ----------------"

    def run(self):
        while not self.md["shutdown"]:
            self.run_impl()

        self.cleanup()

    def run_impl(self):
        time.sleep(10)
        if self.md["update_alarms"]:
            self.alarms = self.md["alarms"]
            self.md["update_alarms"] = False

        # TODO: implement day-check
        now = datetime.datetime.now()

        for a in self.alarms:
            if a.hour == now.hour and a.minute == now.minute:
                print "ALARM - ALARM - ALARM - ALARM"
                mixer.init()
                mixer.music.load()
                mixer.music.play()


        print "[Runner]."

    def cleanup(self):
        print "Runner cleaning up"

