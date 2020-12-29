import numpy as np

from helpers import trexp

# Constraints used in all of the problems

def c1(p, u, P, **kwargs):
    return (p * u ** 2).sum() - P

def c2(x, u, T, C, **kwargs):

    '''
        Here we use a surrogate for exp(x/4) using

            \[ \sum_{i=0}^\infty \frac{x^i}{i!} \]

        i.e the Maclaurin series expansion of $\exp(x)$ the constraint is

            \[ \sum_{i=1}^5 c_i(x_i) (u_i \exp(u_i / 4)) \leq C \]
    '''

    # (C)ost (R)eliability (R)elation function
    def crr(x, t, **kwargs):
        # $\alpha_i * (-t / log(x_i))^beta_i \forall i$
        return (T['alpha-e5'] / 1e5) * (-t / np.log(x)) ** T['beta']

    return (crr(x, **kwargs) * (u + trexp(u / 4))).sum() - C

def c3(w, u, W, **kwargs):
    return (w * u * trexp(u / 4)).sum() - W
