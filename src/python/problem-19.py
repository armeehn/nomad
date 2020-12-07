import numpy as np
import pandas as pd
from functools import reduce

import sys

from helpers import R
from constraints import *

# Test Problem 19: Bridge System

dim = 5     # Dimension of x (and u)

if len(sys.argv) < 2:
    # There isn't a file to open
    exit(1)

filename = sys.argv[1]
with open(filename) as f:

    contents = f.readline().split()

    # Type cast to respective types
    x = np.array([ float(a) for a in contents[:dim] ])
    u = np.array([ int(a) for a in contents[dim:] ])

# Given data

t = 1000    # Time required for the system to be fault tolerant
C = 175     # Cost parameter
P = 110     # Reliability parameter
W = 200     # Not sure what this is...

T = pd.DataFrame(columns = ['i', 'alpha-e5', 'p', 'w', 'beta'])

T['alpha-e5'] = [2.330, 1.450, 0.541, 8.050, 1.950]
T['p'] = [1, 2, 3, 4, 2]
T['w'] = [7, 8, 8, 6, 9]
T['beta'] = dim * [1.5]

config = [  [1, [0, 1]],
            [1, [2, 3]],
            [1, [0, 3, 4]],
            [1, [1, 2, 4]],
            [2, [0, 1, 2, 3, 4]],
            [-1, [0, 1, 2, 3]],
            [-1, [0, 1, 2, 4]],
            [-1, [0, 1, 3, 4]],
            [-1, [0, 2, 3, 4]],
            [-1, [1, 2, 3, 4]],
        ]

# Objective function, the main ingredient
# Note that we are looking to maximize, so we minimize -f.
def f(x, u):

    # No need to recompute in the loop
    Rs = R(x, u)

    # Get your fun(c/k)tional on
    # Note: this can be reduced further...
    sum = 0
    for (c, mask) in config:
        sum += c * reduce(lambda a, b: a * b, Rs[mask])

    return sum

# Main call
if __name__ == '__main__':
    p, w = T['p'].values, T['w'].values
    # Note that we are looking to maximize, so we minimize -f.
    out = (     -f(x, u),
                c1(p, u, P=P),
                c2(x, u, t=t, C=C, T=T),
                c3(w, u, W=W),
            )
    print('%4.3f %4.3f %4.3f %4.3f' % out)
