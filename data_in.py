#!/usr/bin/python3
from RPi.GPIO import *
import time

class Datalines:
    def __init__(self, negative, positive, button):
        self.data0 = negative
        self.data1 = positive
        self.button = button
        setmode(BOARD)
        setwarnings(False)
        setup(self.data0, IN)
        setup(self.data1, IN)
        setup(self.button, IN)

    def watch(self, name):
        start = time.time()
        capture = ''
        print(name)
        print('')
        while input(self.button) == 0:
            if time.time() - start > 1:
                start = time.time()
                if capture != '':
                    print(hex(int(int(capture, 2))))
                    capture = ''
            if input(self.data0) == LOW:
                capture += '0'
            elif input(self.data1) == LOW:
                capture += '1'

    def watch_improved(self, name):
        start = time.time()
        capture = ''
        print(name)
        print('')
        while input(self.button) == 0:
            if time.time() - start > 1:
                start = time.time()
                if capture != '':
                    print(hex(int(int(capture, 2))))
                    capture = ''
            if input(self.data0) == LOW:
                capture += '0'
                #time.sleep(.00005)
                time.sleep(.0000005)
            elif input(self.data1) == LOW:
                capture += '1'
                time.sleep(.0000005)


umm = Datalines(13,15,16)
umm.watch_improved('Five')
 
