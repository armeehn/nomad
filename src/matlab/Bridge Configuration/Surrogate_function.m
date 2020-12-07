clc;
clear;
close all;

%% Variable Definition
tic
x0 = [ 0.1 0.1 0.1 0.1 0.1 1 1 1 1 1 ]';            %Starting Point

l = 10^-6;

lb = [ l l l l l 1 1 1 1 1 ]';                      %Lower Bound

ub = [ 1-l 1-l 1-l 1-l 1-l 10 10 10 10 10 ]';       %Upper Bound

%% Options

opts = nomadset('display_degree',2,'bb_output_type','OBJ PB PB PB',...
    'bb_input_type','( R R R R R I I I I I )','max_bb_eval',300,...
    'has_sgte',1); 

%% Start optimization
[x,fval] = nomad(@func_surrogate_bridge,x0,lb,ub,opts);
toc