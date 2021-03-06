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

'''In [2]: x, y, z = symbols('x y z')
In [5]: diff(x**2+2*x)
Out[5]: 2*x + 2

In [6]: diff(2*x + 2)
Out[6]: 2'''

def f(x):
    return x**2 + 2x

def df(x):
    return 2*x + 2

def ddf(x):
    return 2

F = [f, df, ddf]
F_names = ["$f$", "$f'$", "$f''$"]

fig, axs = plt.subplots(3, figsize=(14, 8))

x = np.linspace(-4, 2, num=200)
for i, (ax, function) in enumerate(zip(axs, F)):
    ax.plot(x, function(x), linewidth=3)
    ax.set_title(F_names[i])

fig.tight_layout()

'''
Q: Using Newton's Method for optimization, write a function that returns one of the local minimas of the quartic function $f(x) = x^4 + 2x^3 - 5x^2 - 8$.
   As stated in the description, to use Newton's method we conceptualize the problem finding zeros of the derivative. This requires us competing the derivative and the second derivative.

def f(x):
    return x**4 + 2 * x**3 - 5 * x**2 - 8

def df(x):
    return 4 * x**3 + 6 * x**2 - 10 * x

def ddf(x):
    return 12 * x**2 + 12 * x - 10

F = [f, df, ddf]
F_names = ["$f$", "$f'$", "$f''$"]
'''
