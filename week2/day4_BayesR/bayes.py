import matplotlib.pyplot as plt
import random

def dice_likelihood(data, num_sides):
    if data > num_sides:
        return 0
    else:
        return 1/num_sides

def roll_die(sides):
    result = random.randint(1, sides)
    return result   

class Bayes(object):
    '''
    INPUT:
        prior (dict): key is the number of outcomes (e.g. 4-sided die),
                      value is the probability

        likelihood_func (function): takes a new piece of data and the value and
                                    outputs the likelihood of getting that data
    '''
    def __init__(self, prior = {4:.2, 6:.2, 8:.2, 12:.2, 20:.2}, likelihood_func = dice_likelihood):
        self.prior = prior
        self.likelihood = likelihood_func

    def normalize(self, data):
        '''
        INPUT: None
        OUTPUT: None

        Makes the sum of the probabilities equal 1.
        '''
        norm_constant=0
        for key in self.prior:
            norm_constant += self.likelihood(data, key)*self.prior[key]
        return norm_constant

    def update(self, data):
        '''
        INPUT:
            data (int or str): A single observation (data point)

        OUTPUT: None

        Conduct a bayesian update. Multiply the prior by the likelihood and
        make this the new prior.
        '''

        norm_c = self.normalize(data)
        for key in self.prior:
            self.prior[key] = self.likelihood(data, key)*self.prior[key]/norm_c
        self.print_distribution()

    def print_distribution(self):
        '''
        Print the current posterior probability.
        '''
        print(self.prior)

    def multi_update(self, sides, num_rolls):
        for r in range(num_rolls):
            self.update(roll_die(sides))

    def plot(self, color=None, title=None, label=None):
        '''
        Plot the current prior.
        '''
        pass
