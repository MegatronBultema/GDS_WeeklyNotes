class Fraction(object):
    ''' Makes a fraction object '''

    def __init__(self, num = 0, denom = 1):
        ''' runs when object instantiated '''
        self.num = num
        self.denom = denom

    def __repr__(self):
        ''' tells python how to represent the object '''
        return "{0}/{1}".format(self.num,self.denom)

    def add(self, other):
        ''' defines the add function '''
        if self.denom == other.denom:
            return Fraction(self.num + other.num, self.denom)
        else:
            #lcd=min(list(set(self.multiples(10)).intersection(set(other.multiples(10)))))
            #print(lcd)
            common_denom = self.denom * other.denom
            return Fraction(self.num*other.denom + other.num*self.denom, common_denom)
            #print("The denominators don't match.  Impossible!")
            #return None

    def __add__(self, other):
        ''' overload the + operator '''
        return self.add(other)

    def multiples(self, count):
        for i in range(0,count*self.denom,self.denom):
            print(i)


if __name__ == '__main__':
    f1 = Fraction(num = 2, denom = 3)
    f2 = Fraction(num = 1, denom = 3)

    # What attributes will a Fraction object have?

    # Can I display a Fraction object?  Why or why not?

    # What could be done to allow adding fractions with different denominators?
