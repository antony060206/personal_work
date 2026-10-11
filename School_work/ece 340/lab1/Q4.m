% a) System: y[k] = a*y[k-1] + x[k], with y[k] = 0 for k < 0

% b) 
k = 0 : 50;
x = ones(1, length(k)); 

a1 = 0.5;
a2 = 2;

y1 = sysresp(x, a1);
y2 = sysresp(x, a2);

disp('y[k] for a = 0.5, k = 0..5:');
disp(y1(1:6));

disp('y[k] for a = 2, k = 0..5:');
disp(y2(1:6));

figure;
stem(k, y1, 'filled');
hold on;
stem(k, y2, 'filled');
hold off;
xlabel('k');
ylabel('y[k]');
title('Response y[k] of the DT system for a = 0.5 and a = 2');
legend('a = 0.5', 'a = 2');
grid on;

% c)
    a3 = 0.9;                       % |a| < 1, so the system should be BIBO stable
    y3 = sysresp(x, a3);

    % Verification: compare sysresp against the closed-form step response
    y3_theory = (1 - a3.^(k+1)) / (1 - a3);
    max_err   = max(abs(y3 - y3_theory));

    fprintf('a = %.2f\n', a3);
    fprintf('y[50] computed  = %.4f\n', y3(end));
    fprintf('1/(1-a) limit   = %.4f\n', 1/(1 - a3));
    fprintf('Max deviation from closed form = %.3e\n', max_err);

figure
stem(k, y3, 'filled')
xlabel('k')
ylabel('y[k]')
title(sprintf('Step response for a = %.2f (verifying BIBO stability)', a3))
grid on