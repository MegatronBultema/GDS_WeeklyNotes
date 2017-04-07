#classes_mysoln.py

import numpy as np

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        dis=np.sqrt((self.x-other.x)**2 + (self.y - other.y)**2)
        return dis


    def __repr__(self):
        return '{},{}'.format(self.x, self.y)



class Triangle(object):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __repr__(self):
        return 'Triangle with points ({},{}) , ({},{}), ({},{})'.format(self.p1.x, self.p1.y,self.p2.x, self.p2.y,self.p3.x, self.p3.y)

    def perimeter(self):
        d12=self.p1.distance(self.p2)
        d23=self.p2.distance(self.p3)
        d31=self.p3.distance(self.p1)
        return d12+d23+d31

    def is_line(self):
        #return a==self.p1 and b==self.p2 and c==self.p3
        return self.perimeter()==0


def main():
    p1 = Point(9,2)
    p2 = Point(5,5)
    print('distance, {}'.format(p1.distance(p2)))


if __name__ == '__main__':
    main()
