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

    def watch_improved(self):
        start = time.time()
        capture = ''
        switch = False
        while input(self.button) == 0:
            if not switch and capture != '':
                print("hexidecimal: " + hex(int(int(capture, 2))))
                print("binary: " + bin(int(capture,2)))
                print("decimal: " + str(int(capture,2)))
                print("length: " + str(len(capture)))
                capture = ''
            
            if input(self.data0) == LOW:
                capture += '0'
                time.sleep(.0000005)
                switch = True
                start = time.time()
            elif input(self.data1) == LOW:
                capture += '1'
                time.sleep(.0000005)
                switch = True
                start = time.time()
            elif time.time() - start > .5:
                switch = False


umm = Datalines(13, 15, 16)
umm.watch_improved()
 
