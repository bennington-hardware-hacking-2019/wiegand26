#!/usr/bin/python3
from RPi.GPIO import *
import time

class Datalines:
    def __init__(self, negative, positive):
        self.data0 = negative
        self.data1 = positive
        setmode(BOARD)
        setwarnings(False)
        setup(self.data0, IN)
        setup(self.data1, IN)

    def watch(self):
        start = time.time()
        capture = ''
        pos = (9,26)
        while True:
            if input(self.data0) == LOW:
                capture += '0'
                time.sleep(float(sys.argv[3]))
                start = time.time()
            elif input(self.data1) == LOW:
                capture += '1'
                time.sleep(float(sys.argv[3]))
                start = time.time()
            elif time.time() - start > .5 capture != '':
                print("Card Number: " + str(int(capture[pos[0]:pos[1]], 2)))
                break



umm = Datalines(15, 13)
umm.watch()
 
