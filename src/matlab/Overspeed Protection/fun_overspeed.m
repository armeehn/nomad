function [ fout ] = fun_overspeed(X)

%% Variables Definition
x = X(1:4);
u =X(5:8);
n = 4;
p = [1,2,3,2];
w = [6,6,8,7];
beta = 1.5*ones(1,n);
alpha = [1,2.3,0.3,2.3]/10^5;
t = 1000;
P = 250;
W = 500;
C = 400;

%% Constraints for true objective function
c1 = 0;
c2 = 0;
c3 = 0;

%% Computing the realibility at stage i and the cost reliability function
for i = 1:n
    R(i) = 1-(1-x(i))^u(i);
    c(i) = alpha(i)* (-t/log(x(i)))^beta(i);
   
end

%%  objective
obj= prod(R);
%% constraints
for m=1:n
    
    c1 = c1+(p(m)*u(m)^2);
    c2 = c2+(c(m)*(u(m)+exp(u(m)/4)));
    c3 = c3+(w(m)*u(m)*exp(u(m)/4));
    
end
c1 = c1-P;
c2 = c2-C;
c3 = c3-W;
%% Output function and constraints
fout=[-obj , c1 , c2 , c3];
end
