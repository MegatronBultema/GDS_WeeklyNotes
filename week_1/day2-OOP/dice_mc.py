import numbers
import numpy as np

class NDice(object):
    ''' Makes a dice object '''

    def __init__(self, nsides=3):
        '''Runs when dice is instantiated. Default is a three sided dice'''
        self.nsides = nsides
        self.up= np.random.choice(np.arange(1,self.nsides+1))
        print(self.up)

    def sides(self):
        '''returns the number of sides the dice has'''
        return self.nsides

    def faceup(self):
        ''' returns a random selection of the possible values to represent the
        face of the die that is up'''
        return self.up

    def roll_die(self):
        self.up = np.random.choice(np.arange(1,self.nsides+1))
        return self.up

# need to add comparison majic methods
    def __lt__(self, other):
        return self.up < other.up

    def __eq__(self,other):
        return self.up == other.up

    def __le__(self,other):
        return self.up <= other.up

    def __gt__(self, other):
        return self.up > other.up

    def __ge__(self,other):
        return self.up >= other.up
    #def __bool__(self)
    #    if x:

    def __ne__(self, other):
        return self.up != other.up
    
