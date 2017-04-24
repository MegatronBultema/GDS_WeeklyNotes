'''
This file will give code and explinations to the normal distribution as
implimented in scipy.stats.

The probaility density function (probability )


'''
import scipy.stats as scs
import matplotlib.pyplot as plt
import numpy as np
import math
plt.close()


# make a, a normal distribution with a mean (loc) of 1 and a
#standard deviation (scale) of 2
a = scs.norm(loc=1, scale = 2)

#the probability density function of a single value x gives probability that
#value would be chosen at random from the above normal distribution
a.pdf(1)

#the cumulative density function gives the cumulative density (integration under pdf curve) up to the given value x
a.cdf(1)

#the percentil point function returns the value x corresponding to the given cumulative
#probability density. below will return a value of x. the probability of randomly selecting a value x below that value returned is 95%.
a.ppf(0.95)

'''
The equation is m/(1+exp((-(t-c))/s))
c=center s=scale m=maximum rate
'''

def sigmoid(x,s):
    a = []
    for item in x:
        a.append(1/(1+math.exp(-item/s)))
    return a


def plot_logistic (xstart=0.5, xend=3):
    fig, ax = plt.subplots(1,1)
    for s in np.arange(xstart, xend, 0.5):
        x = np.arange(-10., 10., 0.2)
        sig = sigmoid(x,s)
        lbl='sigmoid curve with s={}' .format(s)
        ax.plot(x, sig, lw = 3, label=lbl)
        ax.legend(loc=lbl)
    plt.show()
    plt.savefig('sigmoid curve')

def plot_normal(mean=0, stddev=1):
    # normal distribution (standardized), DOES NOT DEPEND ON NUMBER OF SAMPLES
    # inputs
    norm_dist = scs.norm(loc=mean, scale = stddev) # standardized normal distribution
    plot_min_x = norm_dist.ppf(0.005) # plot from 0.5% of area
    plot_max_x = norm_dist.ppf(0.995) # to 99.5% of area
    num_x_vals = 200
    # set our limits based on our desired significance level
    z1 = norm_dist.ppf(0.025) # z value at 2.5% of area
    z2 = norm_dist.ppf(0.975) # z value at 97.5% of area
    # set the critical value
    z_cr = norm_dist.ppf(0.99)

    "make the plot"
    x_norm = np.linspace(plot_min_x, plot_max_x, num_x_vals)
    y_norm = norm_dist.pdf(x_norm)
    fig, ax = plt.subplots(1,1)
    lbl = "normal pdf"
    ax.plot(x_norm, y_norm, lw = 3, label=lbl)
    ax.legend(loc = 'best')
    plt.axvline(x = z1, lw = 1, color = 'k')
    plt.axvline(x = z2, lw = 1, color = 'k')
    plt.axvline(x = z_cr, lw = 3, color = 'r')
    plt.xlabel('z value')
    plt.ylabel('normal pdf')
    plt.savefig('norm_dist.png')
    plt.close()

'''
In terms of sample estimation: the distribution of any random sample from an underlying distribution (if large enough) will approach a normal distirbution.<-- Central Limit Therum
'''
