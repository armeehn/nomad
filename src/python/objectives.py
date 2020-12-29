from functools import reduce

from helpers import R

def f19(x, u):
    
    # Test Problem 19: Bridge System
    # Representation of the objective

    config = [  [1,  [0, 1]],
                [1,  [2, 3]],
                [1,  [0, 3, 4]],
                [1,  [1, 2, 4]],
                [2,  [0, 1, 2, 3, 4]],
                [-1, [0, 1, 2, 3]],
                [-1, [0, 1, 2, 4]],
                [-1, [0, 1, 3, 4]],
                [-1, [0, 2, 3, 4]],
                [-1, [1, 2, 3, 4]],
            ]

    # No need to recompute in the loop
    Rs = R(x, u)

    # Get your fun(c/k)tional on
    # Note: this can be reduced further...
    sum = 0
    for (c, mask) in config:
        sum += c * reduce(lambda a, b: a * b, Rs[mask])

    return sum

# Test Problem 20: Overspeed Protection System
f20 = lambda x, u: reduce(lambda a, b: a * b, R(x, u))

def f21(x, u):

    # Test Problem 21: Series-Parallel System

    a = 1 - R(x[0], u[0]) * R(x[1], u[1])
    b = 1 - (1 - R(x[2], u[2])) * (1 - R(x[3], u[3])) * R(x[4], u[4])

    return 1 - a * b

def wrapper(problem_id):

    # Trivial wrapper to make it nicer

    if problem_id == 'problem-19':
        return f19
    elif problem_id == 'problem-20':
        return f20
    elif problem_id == 'problem-21':
        return f21
    else:
        raise ValueError("No problem exists for this problem ID!")
