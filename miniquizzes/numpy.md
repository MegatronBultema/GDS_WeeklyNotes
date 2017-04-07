## Miniquiz: Appreciating Numpy

**Include your code and answers in** `numpy_quiz.py`.

1. Write a python function to find the value in a list that's closest to a given value.

    e.g. `closest([10, 17, 2, 29, 16], 14)` should return 16.

2. Instead let's start with a numpy array. How can we do the same thing in one line using numpy magic?

    Hint: Use `np.abs` and `np.argmin`.

3. My favorite numpy trick is [masking](http://docs.scipy.org/doc/numpy/user/basics.indexing.html#boolean-or-mask-index-arrays). Say you have a feature matrix `X` (2d numpy array) and with labels `y` (1d numpy array). I would like to get a feature matrix of only the positive cases, i.e. get the rows from `X` where `y` is positive.

    How can you do this in one line?
    
    Create example `X` and `y` to verify your code.
