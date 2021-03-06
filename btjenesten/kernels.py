#Authors: Christian Elias Anderssen Dalan <ceadyy@gmail.com>
#With the help of Audun Skau Hansen <a.s.hansen@kjemi.uio.no>
#April 2022

import numpy as np

def RBF(X1, X2, l = 1):
    """
    Radial basis function of the form:
    $$
    e^{-l * d(X_i,X_j)}
    $$

    Parameters:
    -----------
    X1: Dataset 1
    
    X2: Dataset 2

    l: Length scale parameter. 
    Can be adjusted to adjust the covariance between $x_i$ and $x_j$. 
    Increasing l will decrease the covariance, and vice verca.

    Returns:
    -----------
    A matrix with the same shape as our input data, where the elemets are:
    $e^{-l*d(x_i, x_j)}$ where $d(x_i, x_j)$ is the difference between element $x_i$ in X1
    and element $x_j$ in X2.
    """

    return np.exp(-l*(X1[:, None] - X2[None,:])**2)

def Constant(X1, X2, k = 0.5):
    """
    Kernel that returns a constant covariance value between $x_i$ and $x_j$
    Useful if all values depend on eachother equally.

    Parameters:
    -----------
    X1: Dataset 1

    X2: Dataset 2

    k: constant that determines the covariance.

    Returns:
    A matrix with the same shape as our input data. All matrix elements have the value k.
    """

    return np.ones(X1.shape)*k

def Funny_trigonometric(X1, X2, k = 1):
    """
    Kernel that I made only for fun. May work for extravagant datasets

    Parameters:
    -----------
    X1: Dataset 1

    X2: Dataset 2

    k: constant that determines the frequency of the trigonometric functions.

    Returns:
    A covariance matrix that might be a bit crazy.
    """

    return np.sin(-k*(x[:, None] - y[None,:])**2) - np.cos(-k*(x[:, None] - y[None,:])**2)