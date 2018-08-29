import numpy as np
from numpy import exp, array, random, dot

def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1-x)
    return 1/(1+exp(-x))

# Input data
X = np.array([[0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1]])

# Output data
y = np.array([[0],
            [1],
            [1],
            [0]])

