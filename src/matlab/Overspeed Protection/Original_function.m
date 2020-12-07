clc;
clear;
close all;

%% Variable Definition
tic
x0 = [0.5 0.5 0.5 0.5 1 1 1 1 ]';                           %Starting Point

lb = [0.5 0.5 0.5 0.5  1 1 1 1 ]';          %Lower Bound

ub = [1-10^-6 1-10^-6 1-10^-6 1-10^-6  10 10 10 10 ]';       %Upper Bound

%% Options
opts = nomadset('display_degree',2,'bb_output_type','OBJ PB PB PB',...
    'bb_input_type','( R R R R I I I I )','max_bb_eval',300); 

%% Start optimization
[x,fval] = nomad(@fun_overspeed,x0,lb,ub,opts);
toc