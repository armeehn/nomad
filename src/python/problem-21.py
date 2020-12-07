import numpy as np
import pandas as pd
from functools import reduce

import sys

from helpers import R
from constraints import *

# Test Problem 21: Series-Parallel System

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
P = 180     # Reliability parameter
W = 100     # Not sure what this is...

T = pd.DataFrame(columns = ['alpha-e5', 'p', 'w', 'beta'])

T['alpha-e5'] = [2.5, 1.450, 0.541, 0.541, 2.1]
T['p'] = [2, 4, 5, 8, 4]
T['w'] = [3.5, 4.0, 4.0, 3.5, 4.5]
T['beta'] = dim * [1.5]


def f(x, u):

    a = 1 - R(x[0], u[0]) * R(x[1], u[1])
    b = 1 - (1 - R(x[2], u[2])) * (1 - R(x[3], u[3])) * R(x[4], u[4])

    return 1 - a * b

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
