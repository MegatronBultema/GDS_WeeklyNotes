import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sympy import *

#1
X, y = make_classification(n_samples=100,
                            n_features=2,
                            n_informative=2,
                            n_redundant=0,
                            n_classes=2,
                            random_state=0)

#2
fig, ax = plt.subplots()
colors = [(.255*i,i, .255*i, 1) for i in y]
ax.scatter(X[:,1], X[:,0], c=colors)
#3
#A very small negative slope
m = -0.2
plt.plot(X[:,1], m*X[:,1])
plt.savefig("scatter_features.png")


#PART 2


beta = np.array([1,1]).T

def h(row,beta):
    hv=1/(1+np.exp(-(beta[0]*row[0] + beta[1]*row[1])))
    return hv

def cost(row):
    beta=[1,1]
    y=row[2]
    cost=y*log(h(row,beta))+(1-y)*log(1-h(row,beta))
    return cost


x1=[0,1,1]
x2=[2,2,0]
x3=[3,0,0]

p1 = cost(x1)
p2 = cost(x2)
p3 = cost(x3)
print(p1+p2+p3)
