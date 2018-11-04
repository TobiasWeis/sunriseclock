#!/usr/bin/python
'''
author: Tobias Weis
'''

import multiprocessing
import time

class Runner(multiprocessing.Process):
    def __init__(self, config, md, alarms):
        multiprocessing.Process.__init__(self)
        self.config = config
        self.md = md

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
        print "[Runner]."

    def cleanup(self):
        print "Runner cleaning up"

