#!/usr/bin/env python
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from neopixel import *
import numpy as np
import argparse


class SunriseController:
    def __init__(self):
        # LED strip configuration:
        #LED_COUNT      = 300      # Number of LED pixels.
        LED_COUNT      = 5      # Number of LED pixels.
        LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
        #LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
        LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
        LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
        LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
        LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

        # Create NeoPixel object with appropriate configuration.
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()


    def cleanup(self):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i,0)
        self.strip.show()


    def sunrise(self, duration):
        """
        every colum should have the last colors of above sunrise colors
        duration: time in minutes
        """
        colors = np.array([
                [0.48131050850748586, 0.9167970679655845, 1.0] ,
                [0.5948093609673182, 0.9363570656387129, 1.0] ,
                [0.6730759959206745, 0.9481700147278443, 1.0] ,
                [0.7344334434940258, 0.9550471130827453, 1.0] ,
                [0.786233792687932, 0.9584992709042172, 1.0] ,
                [0.8321593871755296, 0.9594000907706687, 1.0] ,
                [0.8743087446266337, 0.9582779247096972, 1.0] ,
                [0.913990141184712, 0.9554582957500269, 1.0] ,
                [0.9520782896860697, 0.9511386309282809, 1.0] ,
                [0.9891938096837013, 0.9454294694115567, 0.9334589953027584] ,
                [1.0, 0.938377708732323, 0.8660070372618588] ,
                [1.0, 0.9299794480368715, 0.8012000142190369] ,
                [1.0, 0.920186230004245, 0.7383136038438242] ,
                [1.0, 0.9089065532347129, 0.6766653046124846] ,
                [1.0, 0.896003407058198, 0.6155638341825179] ,
                [1.0, 0.8812877888327108, 0.554244474355265] ,
                [1.0, 0.8645074168715645, 0.49176738424764327] ,
                [1.0, 0.8453289032241411, 0.4268246451948009] ,
                [1.0, 0.823310157603532, 0.35729855291741025] ,
                [1.0, 0.7978571148817347, 0.27897652183973887] ,
                [1.0, 0.76815360116612, 0.1798571282261793] ,
                [1.0, 0.7330418033095352, 0.0] ,
                [1.0, 0.6908038056878648, 0.0] ,
                [1.0, 0.6387215839285414, 0.0] ,
                [1.0, 0.5720565218237464, 0.0] ,
                [1.0, 0.48108666765593483, 0.0] ,
                [1.0, 0.33777348074405444, 0.0] ,
                [1.0, 0.0, 0.0] ,
                [1.0, 0.0, 0.0] ,
                [1.0, 0.0, 0.0] ,
                [0.6, 0.0, 0.0],
                [0.4, 0.0, 0.0],
                [0.3, 0.0, 0.0],
                [0.2, 0.0, 0.0]
        ])

        colors = (colors*255).astype(np.uint8)
        numcols = 1
        numrows = 5 

        numsteps = len(colors)-numrows
        stepduration = (duration*60)/numsteps

        for step in range(numsteps):
            for y in range(numrows):
                for x in range(numcols):
                    col = colors[len(colors)-1-y-step]
                    self.strip.setPixelColor(x*numrows+y, Color(col[1],col[0],col[2]))
            self.strip.show()
            time.sleep(stepduration)

            print "Next step!"
            #time.sleep(1)

if __name__ == "__main__":
    sc = SunriseController()
    sc.sunrise()
    sc.cleanup()
