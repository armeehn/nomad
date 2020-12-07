clc;
clear;
close all;

%% Variable Definition
tic
n = 15;
a = 0.5;
b = 1-10^-6;

x = a+(b-a)*rand(1,n);

u =  randi([1,10],1,n);

x0 = [x u]';                            %Starting Point

lb = [a*ones(1,n) ones(1,n)]';          %Lower Bound
ub = [b*ones(1,n) 10*ones(1,n)]';       %Upper Bound


%% Options

opts = nomadset('display_degree',2,'bb_output_type','OBJ PB PB PB',...
    'bb_input_type','( R R R R R R R R R R R R R R R  I I I I I I I I I I I I I I I  )',...
    'max_bb_eval',300,'has_sgte',1); 


%% Start optimization
[x,fval] = nomad(@func_30,x0,lb,ub,opts);
toc