import numpy as np
import pandas as pd
from functools import reduce

import sys

from helpers import R
from constraints import *

# Test Problem 20: Overspeed Protection System

dim = 4     # Dimension of x (and u)

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
C = 400     # Cost parameter
P = 250     # Reliability parameter
W = 500     # Not sure what this is...

T = pd.DataFrame(columns = ['alpha-e5', 'p', 'w', 'beta'])
T['alpha-e5'] = [1.0, 2.3, 0.3, 2.3]
T['p'] = [1, 2, 3, 2]
T['w'] = [6, 6, 8, 7]
T['beta'] = dim * [1.5]

# Objective function, the main ingredient
f = lambda x, u: reduce(lambda a, b: a * b, R(x, u))

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
