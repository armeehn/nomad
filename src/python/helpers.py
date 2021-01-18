import numpy as np

R = lambda x, u: 1 - (1 - x) ** u

def trexp(x, N=3):

    '''
        Truncation of the exponential function
        using a boolean-like mask
    '''

    b = np.zeros(4)
    b[:N] = 1.
    summands = np.array([   1,
                            x,
                            x ** 2 / 2,
                            x ** 3 / 6,
                        ])

    return (b * summands).sum()
