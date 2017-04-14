'''
Suppose you are interested in testing if, on average, a bottle of coke weighs 20.4 ounces. You have collected a
simple random sample of 130 bottles of coke and weighed them.
Ho: average weight of samples equals 20.4 oz
Ha: average weight of samples does not weigh 20.4 oz

 State why you are able to apply the Central Limit Theorem (CLT) here to approximate the sampling distribution to be normal.


'''
import numpy as np
import scipy.stats as scs
import matplotlib.pyplot as plt

a=np.loadtxt('power-bayesian/data/coke_weights.txt')
mean_a=a.mean()
sem_a=scs.sem(a)
r=scs.norm.rvs(loc=mean_a, scale=sem_a, size=1000)
rnorm=scs.norm(loc=20.4, scale=sem_a)
snorm=scs.norm(loc=mean_a, scale=sem_a)
rpdf=scs.norm.pdf(r, loc=0, scale=1)
fig = plt.figure()

pdf_range = np.linspace(mean_a-4*sem_a,mean_a+4*sem_a, 1000)
pdf_range1 = np.linspace(20.4-4*sem_a,20.4+4*sem_a, 1000)
ax = fig.add_subplot(1,1,1)
ax.plot(pdf_range1, rnorm.pdf(pdf_range1),c='#FF0099', lw=4, label='pdf')
ax.plot(pdf_range, snorm.pdf(pdf_range))
ax.axvline(20.4, c='#FF0099')
ax.axvline(mean_a)

z=scs.norm.ppf(0.975)
#plt.axvline(20.4+sem_a*z, lw = 1, color = 'k')
#plt.axvline(20.4-sem_a*z, lw = 1, color = 'k')
'''
because the sample mean falls within the bounds we are not confident that the sample mean is different than the random distribution.
'''

plt.axvline(mean_a+sem_a*z, lw = 1, color = 'r')
plt.axvline(mean_a-sem_a*z, lw = 1, color = 'r')
'''
Build a 95% confidence interval based on the sample data. Does your interval suggest that the weight of a bottle of coke is different than 20.4 ounces? Explain what a false negative is in the context of this problem.
'''

plt.show()

    # t distribution
    # inputs
df = 130 # degrees of freedom of t distribution
t_dist = scs.t(df) # standardized t distribution
'''
plot_min_x = t_dist.ppf(0.005) # plot from 0.5% of area, find the t value that cooresponds to 0.5% area under the surve
plot_max_x = t_dist.ppf(0.995) # to 99.5% of area
'''
num_x_vals = 200
    # set our limits based on our desired significance level
t1 = t_dist.ppf(0.025, loc=20.4) # t value at 2.5% of area
t2 = t_dist.ppf(0.975, loc=20.4) # t value at 97.5% of area
    # set the critical value, comes out of test stat

t_cr = t_dist.ppf(0.99)+20.4

plt.axvline(x = t1, lw = 1, color = 'k')
plt.axvline(x = t2, lw = 1, color = 'k')
plt.axvline(x = t_cr, lw = 3, color = 'r')
plt.xlabel('t value')
plt.ylabel('t pdf')
#ax.set_xlim((-20,20))
#ax.set_ylim((0,0.5))


#ax2.hist(r)
#pdf_range1 = np.linspace(scs.norm.ppf(0.01),scs.norm.ppf(0.99), 100)
#pdf_range2 = np.linspace(scs.norm.ppf(0.01),scs.norm.ppf(0.99), 1000)
