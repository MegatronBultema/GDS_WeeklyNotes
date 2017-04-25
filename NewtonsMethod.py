'''##Gradient Descent Review

1. Gradient descent is a technique that finds the minimum solution of a function.
   In this case, we can assume the solution is minimum when the gradient of the
   solution is 0 or close to 0.

   Write a function that would solve `f(x) = x^2 + 2x`.

   In machine learning, this function is often a loss/error function and you are
   trying to find the solution that would minimize error.

   Okay so need to find the partial deriviative'''
from sympy import *
import matplotlib.pyplot as plt
import numpy as np


'''In [2]: x, y, z = symbols('x y z')
In [5]: diff(x**2+2*x)
Out[5]: 2*x + 2

In [6]: diff(2*x + 2)
Out[6]: 2'''

def f(x):
    return x**2 + 2*x

def df(x):
    return 2*x + 2

def ddf(x):
    return 2

#F = [f, df, ddf]
#F_names = ["$f$", "$f'$", "$f''$"]
F = [f, df]
F_names = ["$f$", "$f'$"]

fig, axs = plt.subplots(3, figsize=(14, 8))

x = np.linspace(-4, 2, num=200)
for i, (ax, function) in enumerate(zip(axs, F)):
    ax.plot(x, function(x), linewidth=3)
    ax.set_title(F_names[i])

fig.tight_layout()

def newtons_method_one_dim(f, df, x0, tol=0.01, max_iter=100):
    """Approximate a zero of the one dimensional function f
    using Newton's method.
    """
    x_current = x0
    f_current = f(x_current)
    df_current = df(x_current)
    for i in xrange(max_iter):
        if abs(f_current) <= tol:
            return x_current, f_current
        x_current = x_current - (f_current/df_current)
        f_current = f(x_current)
        df_current = df(x_current)
    print("Max iterations reached.  Returning current position.")
    return x_current, f_current

minimum = newtons_method_one_dim(df, ddf, -3.0)
minimum = (-1.0, 0.0)
# this matches my answer by plotting minimum is -1
