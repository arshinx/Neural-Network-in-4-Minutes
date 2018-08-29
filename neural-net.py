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

np.random.seed(1)

# Synapses
syn0 = 2 * np.random.random((3,4)) - 1
syn1 = 2 * np.random.random((4,1)) - 1

# Training Step
for j in xrange(60000):
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
