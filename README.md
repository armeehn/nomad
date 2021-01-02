# nomad
Public repository for the course project in MATH 562 (Derivative-Free Optimization) @ UBC through the course textbook [1]

## Project description
In this project, we explore the NOMAD software framework developed at GERAD. This exploration is done via the usage of surrogates functions.
Examples used were those that dealt with _reliability and redundancy_ in [2] (initially found in Juliane Müller's PhD thesis then published as article [2]) 

## Code
The code for the project was implemented in both Python and MATLAB by myself and my project partner respectively. This was done in other to cross reference some results over `n = 30` runs for `bb_eval = 100, 200, 300` blackbox evaluations. The Python experimental testing made use of the `$RANDOM` pseudo-random number generator to get a different seed for NOMAD for each test.

## Write-up
A small write-up which intends to be used as somewhat of script is included. The project required filming of a presentation and writing the script smoothed out the process.

## References
[1] Charles Audet and Warren Hare. Derivative-Free and Blackbox Optimization. Springer International Publishing,
    2017.
    
[2] Juliane Müller, Christine A. Shoemaker, and Robert Piché. \SO-MI: A surrogate model algorithm for
    computationally expensive nonlinear mixed-integer black-box global optimization problems". In: Computers
    & Operations Research 40.5 (2013), pp. 1383{1400. issn: 0305-0548. doi: https://doi.org/10.1016/j.
    cor.2012.08.022. url: http://www.sciencedirect.com/science/article/pii/S0305054812001967.
