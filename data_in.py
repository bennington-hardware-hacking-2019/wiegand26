#!/usr/bin/python3
from RPi.GPIO import *
import time
import sys

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
        pos = (int(sys.argv[1]) - 1,int(sys.argv[2]))

        while input(self.button) == 0:
            if not switch and capture != '':
                """
                done = False
                for beg in range(0, len(capture) - 1):
                    for end in range(beg, len(capture) - 1):
                        pos = (beg, end)
                        possible = capture[pos[0]:pos[1]]
                        if len(possible) == 0:
                            break
                        if experiment == int(possible, 2):
                            print("binary: " + capture[:pos[0]] + '|' + capture[pos[0]:pos[1]] + '|' + capture[pos[1]])
                            print("Card Number: " + str(int(possible, 2)))
                            print("length: " + str(len(possible)))
                            capture = ''
                            done = True
                            break
                    if done:
                        break
                        """
                print("binary: " + capture[:pos[0]] + '|' + capture[pos[0]:pos[1]] + '|' + capture[pos[1]:])
                print("Card Number: " + str(int(capture[pos[0]:pos[1]], 2)))
                print("length: " + str(len(capture[pos[0]:pos[1]])))
                capture = ''
                done = True

            
            if input(self.data0) == LOW:
                capture += '0'
                time.sleep(.0005)
                switch = True
                start = time.time()
            elif input(self.data1) == LOW:
                capture += '1'
                time.sleep(.0005)
                switch = True
                start = time.time()
            elif time.time() - start > .5:
                switch = False


umm = Datalines(13, 15, 16)
umm.watch_improved()
 
