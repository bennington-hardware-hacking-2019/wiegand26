#!/usr/bin/python3
from RPi.GPIO import *

class Datalines:
    def __init__(self, negative, positive, card_present):
        self.data0 = negative
        self.data1 = positive
        self.present = card_present
        setmode(BOARD)
        setwarnings(False)
        setup(self.data0, IN)
        setup(self.data1, IN)
        setup(self.present, IN)
    def watch(self):
        if input(self.present) == 0:
            print("Note")
    

Datalines
 
