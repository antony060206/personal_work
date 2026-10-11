function y = sysresp(x, a)
N = length(x); 
y = zeros(1, N);

y(1) = x(1);

for n = 2 : N
    y(n) = a * y(n-1) + x(n);
end

return
