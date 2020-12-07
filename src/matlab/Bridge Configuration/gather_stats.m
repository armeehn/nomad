% run the function and do some statistics for N = 30 runs
% for 100, 200 and 300 blackbox evals

clc;
clear;
close all;

N = 30;

%% Variable Definition
x0 = [ 0.1 0.1 0.1 0.1 0.1 1 1 1 1 1 ]';            %Starting Point

l = 10^-6;

lb = [ l l l l l 1 1 1 1 1 ]';                      %Lower Bound

ub = [ 1-l 1-l 1-l 1-l 1-l 10 10 10 10 10 ]';       %Upper Bound

for num_bb_eval = [100, 200, 300]
    %% Options
    opts = nomadset('display_degree',2,'bb_output_type','OBJ PB PB PB',...
        'bb_input_type','( R R R R R I I I I I )','max_bb_eval', num_bb_eval,...
        'has_sgte',1);
    
    % allocate some space to hold the data
    data = zeros(1,30);
    for i = 1:N
        %% Start optimization
        [x,fval] = nomad(@func_surrogate_bridge,x0,lb,ub,opts);
        data(i) = fval;
    end
    
    printf('num_bb_eval: %i, mean: %f, var: %f\n', num_bb_eval, mean(data), var(data))
    
end