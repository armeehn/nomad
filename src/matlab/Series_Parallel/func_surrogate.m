function [ fout ] = func_surrogate(X,sur)
if (nargin==1)
    sur=false;
end
%% Variables Definition
x = X(1:5);
u =X(6:10);

n = 5;
p = [2,4,5,8,4];
w = [3.5,4,4,3.5,4.5];
beta = 1.5*ones(1,n);
alpha = [2.5,1.450,0.541,0.541,2.1]/10^5;
t = 1000;
P = 180;
W = 100;
C = 175;

%% Constraints for true objective function
c1 = 0;
c2 = 0;
c3 = 0;
%% Constraints for Surrogate objective function
c4 = 0;
c5 = 0;
c6 = 0;
%% Computing the realibility at stage i and the cost reliability function
for i = 1:n
    R(i) = 1-(1-x(i))^u(i);
    c(i) = alpha(i)* (-t/log(x(i)))^beta(i);
   
end

%% objective
obj = 1-(1-R(1)*R(2))*(1-(1-R(3))*(1-R(4))*R(5)) ;
%% constraints
% True constraints
for m=1:n
    
    c1 = c1+(p(m)*u(m)^2);
    c2 = c2+(c(m)*(u(m)+exp(u(m)/4)));
    c3 = c3+(w(m)*u(m)*exp(u(m)/4));
    
end
c1 = c1-P;
c2 = c2-C;
c3 = c3-W;

% Surrogate constraints
for m=1:n
    
    c4 = c4+(p(m)*u(m)^2);
    c5 = c5+(c(m)*(u(m)+(1+u(m)+u(m)^2/2+u(m)^3/6)));
    c6 = c6+(w(m)*u(m)*(1+u(m)+u(m)^2/2+u(m)^3/6));
    
end
c4 = c4-P;
c5 = c5-C;
c6 = c6-W;

%% Output function and constraints
if (sur)
    fout=[-obj , c4 , c5 , c6];
else
    fout=[-obj , c1 , c2 , c3];
end

end
