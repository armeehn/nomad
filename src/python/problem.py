import numpy as np
import pandas as pd
from functools import reduce

import sys

from helpers import R
from constraints import *
from data import supplied_data
from objectives import wrapper

if len(sys.argv) < 2:
    # There isn't a file to open
    exit(1)

problem_id = sys.argv[1][2:] # hope this works lmao

filename = sys.argv[2]

dim = 4 if problem_id == 'problem-20' else 5

with open(filename) as f:

    contents = f.readline().split()

    # Type cast to respective types
    x = np.array([ float(a) for a in contents[:dim] ])
    u = np.array([ int(a) for a in contents[dim:] ])

dataset = supplied_data[problem_id]
T = dataset['tabular-data']
parameters = dataset['params']
f = wrapper(problem_id)

# Main call
if __name__ == '__main__':
    p, w = T['p'].values, T['w'].values
    # Note that we are looking to maximize, so we minimize -f.
    out = (     -f(x, u),
                c1(p, u, **parameters),
                c2(x, u, T, **parameters),
                c3(w, u, **parameters),
            )
    print('%4.3f %4.3f %4.3f %4.3f' % out)
