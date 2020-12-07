function [ fout ] = fun_bridge(X)
%% Variables Definition
x = X(1:5);
u =X(6:10);

n = 5;
p = [1,2,3,4,2];
w = [7,8,8,6,9];
beta = 1.5*ones(1,n);
alpha = [2.330,1.450,0.541,8.050,1.950]/10^5;
t = 1000;
P = 110;
W = 200;
C = 175;
%% Constraints for true objective function
c1 = 0;
c2 = 0;
c3 = 0;
%% Computing the realibility at stage i and the cost reliability functio
for i = 1:n
    R(i) = 1-(1-x(i))^u(i);
    c(i) = alpha(i)* (-t/log(x(i)))^beta(i);
   
end

%% objective
obj= R(1)*R(2) + R(3)*R(4) + R(1)*R(4)*R(5) + R(2)*R(3)*R(5) -...
    R(1)*R(2)*R(3)*R(4) - R(1)*R(2)*R(3)*R(5) - R(1)*R(2)*R(4)*R(5) - ...
    R(1)*R(3)*R(4)*R(5) -R(2)*R(3)*R(4)*R(5)+2*R(1)*R(2)*R(3)*R(4)*R(5);
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
