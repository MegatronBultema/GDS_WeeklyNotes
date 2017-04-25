import numpy as np


class GradientDescent(object):
    """Preform the gradient descent optimization algorithm for an arbitrary
    cost function.
    """

    def __init__(self, cost, gradient, predict_func,
                 alpha=0.01,
                 num_iterations=10000, fit_intercept = True, standardize = True, delta=.0000001):
        """Initialize the instance attributes of a GradientDescent object.

        Parameters
        ----------
        cost: The cost function to be minimized.
        gradient: The gradient of the cost function.
        predict_func: A function to make predictions after the optimizaiton has
            converged.
        alpha: The learning rate.
        num_iterations: Number of iterations to use in the descent.

        Returns
        -------
        self: The initialized GradientDescent object.
        """
        # Initialize coefficients in run method once you know how many features
        # you have.
        self.coeffs = None
        self.cost = cost
        self.gradient = gradient
        self.predict_func = predict_func
        self.alpha = alpha
        self.num_iterations = num_iterations
        self.fit_intercept = fit_intercept
        self.standardize = standardize
        self.delta = delta

    def fit(self, X, y):
        """Run the gradient descent algorithm for num_iterations repititions.

        Parameters
        ----------
        X: A two dimenstional numpy array.  The training data for the
            optimization.
        y: A one dimenstional numpy array.  The training response for the
            optimization.

        Returns
        -------
        self:  The fit GradientDescent object.
        """
        if self.standardize:
            X = self.standardize_func(X)
        if self.fit_intercept:
            X = self.add_intercept(X)
        coeffs= np.zeros(X.shape[1])
        cost_list = []
        coeffs_list = []
        end=100
        #for i in range(self.num_iterations):
        count = 0
        while end > self.delta:
            #print(self.gradient(X,y,coeffs))
            count += 1
            coeffs = coeffs - self.alpha * self.gradient(X,y,coeffs)
            coeffs_list.append(coeffs)
            cost_list.append(self.cost(X,y,coeffs))
            if len(cost_list) > 2:
                end = abs(cost_list[-1] - cost_list[-2])
        print(count)
        print(end)
        #print("Coeffs List: {}".format(coeffs_list))
        #print("Cost List: {}".format(cost_list))
        self.coeffs = coeffs
        return coeffs

    def standardize_func(self,X):
        return X-X.mean(axis=0)/X.std(axis=0)

    def add_intercept(self, X):
        """Add an intercept column to a matrix X.

        Parameters
        ----------
        X: A two dimensional numpy array.

        Returns
        -------
        X: The original matrix X, but with a constant column of 1's appended.
        """
        return np.insert(X,0,np.ones(len(X)),axis=1)

    def predict(self, X):
        """Call self.predict_func to return predictions.

        Parameters
        ----------
        X: Data to make predictions on.

        Returns
        -------
        preds: A one dimensional numpy array of predictions.
        """
        if self.fit_intercept:
            X = self.add_intercept(X)
        return self.predict_func(X,self.coeffs)
