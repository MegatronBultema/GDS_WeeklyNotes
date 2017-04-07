import numbers
import numpy as np

class NDice(object):
    ''' Makes a dice object '''

def __init__(self, nsides=3):
    '''Runs when dice is instantiated. Default is a three sided dice'''
    self.nsides = nsides

def sides(self):
    '''returns the number of sides the dice has'''
    return self.nsides

def faceup(self):
    ''' returns a random selection of the possible values to represent the
    face of the die that is up'''
    return np.random.choice(self.nsides)

def roll_die(self)
    faceup(self)
