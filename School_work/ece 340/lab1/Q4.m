% b) y[k] = x[k] + a[y-1]

% i) 
% first call to the vector will have nothing


function value = sysresp(y, a)

    value = y + a * y;
end

y = 0;

for k = 0 : 50

    if (k < 0)
        % return 1
    else
        y ; sysresp(y, 0.25);
    end

end
