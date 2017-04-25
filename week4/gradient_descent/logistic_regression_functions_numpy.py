import numpy as np
import matplotlib.pyplot as plt

def predict_proba(X, coeffs):
    """Calculate the predicted conditional probabilities (floats between 0 and
    1) for the given data with the given coefficients.

    Parameters
    ----------
    X: A 2 dimensional numpy array.  The data (independent variables) to use
        for prediction.
    coeffs: A 1 dimensional numpy array, the hypothesised coefficients.  Note
        that the shape of X and coeffs must align.

    Returns
    -------
    predicted_probabilities: The conditional probabilities from the logistic
        hypothosis function given the data and coefficients.

    """

    #hv=1/(1+np.exp(-(coeffs[0]*X[0] + coeffs[1]*X[1])))
    linear_pred = np.dot(X,coeffs)
    hv = 1/(1+np.exp(-linear_pred))
    return hv


def predict(X, coeffs, threas=0.5):
    """
    Calculate the predicted class values (0 or 1) for the given data with the
    given coefficients by comparing the predicted probabilities to a given
    threashold.

    Parameters
    ----------
    X: A 2 dimensional numpy array.  The data (independent variables) to use
        for prediction.
    coeffs: A 1 dimensional numpy array, the hypothesised coefficients.  Note
        that the shape of X and coeffs must align.
    threas: Threashold for comparison of probabilities.

    Returns
    -------
    predicted_class: The predicted class.
    """
    probs = predict_proba(X, coeffs)
    predicted = np.where(probs > threas, 1, 0)
    return predicted



def cost(X, y, coeffs):
    """
    Calculate the logistic cost function of the data with the given
    coefficients.

    Parameters
    ----------
    X: A 2 dimensional numpy array.  The data (independent variables) to use
        for prediction.
    y: A 1 dimensional numpy array.  The actual class values of the response.
        Must be encoded as 0's and 1's.  Also, must align properly with X and
        coeffs.
    coeffs: A 1 dimensional numpy array, the hypothesised coefficients.  Note
        that the shape of X, y, and coeffs must align.

    Returns
    -------
    logistic_cost: The computed logistic cost.
    """
    # cost_sum=0
    # for row in range(len(X)):
    #     cost=y[row]*log(predict_proba(X[row],coeffs))+(1-y[row])*log(1-predict_proba(X[row],coeffs))
    #     cost_sum += cost

    cost=y*np.log(predict_proba(X,coeffs))+(1-y)*np.log(1-predict_proba(X,coeffs))

    return -1*np.sum(cost)

def cost_reg(X, y, coeffs, lamb=1):
    """
    Calculate the logistic cost function of the data with the given
    coefficients.

    Parameters
    ----------
    X: A 2 dimensional numpy array.  The data (independent variables) to use
        for prediction.
    y: A 1 dimensional numpy array.  The actual class values of the response.
        Must be encoded as 0's and 1's.  Also, must align properly with X and
        coeffs.
    coeffs: A 1 dimensional numpy array, the hypothesised coefficients.  Note
        that the shape of X, y, and coeffs must align.

    Returns
    -------
    logistic_cost: The computed logistic cost.
    """
    # cost_sum=0
    # for row in range(len(X)):
    #     cost=y[row]*log(predict_proba(X[row],coeffs))+(1-y[row])*log(1-predict_proba(X[row],coeffs))
    #     cost_sum += cost

    cost=y*np.log(predict_proba(X,coeffs))+(1-y)*np.log(1-predict_proba(X,coeffs))

    lam = lamb * np.sum(coeffs**2)
    return -1*np.sum(cost) + lam


def gradient(X,y,coeffs):
    #gr_sum = 0
    #for row in range(len(X)):
        #gr = (predict_proba(X[row],coeffs) - y[row]) * X[row]
        #gr_sum += gr
    gr = np.dot(X.T, predict_proba(X,coeffs) - y)
    return gr


def gradient_regularized(X,y,coeffs,lamb=1):
    gra = np.dot(X.T, predict_proba(X,coeffs) - y) + (lamb * 2*coeffs)
    return gra

def plot(X,predictions):
    fig, ax = plt.subplots()
    colors = [(.255*i,i, .255*i, 1) for i in predictions]
    ax.scatter(X[:,1], X[:,0], c=colors)
    plt.savefig('temp.png')
