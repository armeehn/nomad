# data for the problems
import pandas as pd

col_keys = ['alpha-e5', 'p', 'w', 'beta']

# Within each problem's 'dataset' with parameters, we have:
# t : Time required for the system to be fault tolerant
# C : Cost parameter
# P : Reliability parameter
# W : Not sure what this is...

# Problem 19

T_19 = pd.DataFrame(columns = col_keys)
T_19['alpha-e5']    = [2.330, 1.450, 0.541, 8.050, 1.950]
T_19['p']           = [1, 2, 3, 4, 2]
T_19['w']           = [7, 8, 8, 6, 9]
T_19['beta']        = 5 * [1.5]

data_19 = {
    'params' : {
            't' : 1000,
            'C' : 175,
            'P' : 110,
            'W' : 200,
        },
    'tabular-data' : T_19,
}

# Problem 20

T_20 = pd.DataFrame(columns = col_keys)
T_20['alpha-e5']    = [1.0, 2.3, 0.3, 2.3]
T_20['p']           = [1, 2, 3, 2]
T_20['w']           = [6, 6, 8, 7]
T_20['beta']        = 4 * [1.5]

data_20 = {
    'params' : {
            't' : 1000,
            'C' : 400,
            'P' : 250,
            'W' : 500,
        },
    'tabular-data' : T_20,
}

# Problem 21

T_21 = pd.DataFrame(columns = col_keys)
T_21['alpha-e5']    = [2.5, 1.450, 0.541, 0.541, 2.1]
T_21['p']           = [2, 4, 5, 8, 4]
T_21['w']           = [3.5, 4.0, 4.0, 3.5, 4.5]
T_21['beta']        = 5 * [1.5]

data_21 = {
    'params' : {
            't' : 1000,
            'C' : 175,
            'P' : 180,
            'W' : 100,
        },
    'tabular-data' : T_21,
}

supplied_data = dict( zip(  ['problem-%d' % i for i in [19, 20, 21]],
                            [data_19, data_20, data_21],
                        )
                    )
