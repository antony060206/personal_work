% Lab 3 - Question 1
% a)
n = 0:10;
h1 = n.*(0.5).^n.*sin(n.*pi/6);

figure;
plot(n,h1);
xlabel('n');
ylabel('amplitude')
title('h_1[n] from the expression (n.*(0.5).^n.*sin(n.*pi/6);)');

%b)
% n2 = (0.25.*n.^-1)-(0.0625.*n.^-3);
% d2 = 1-sqrt(3).*n.^-1+1.25.*n.^-2-(sqrt(3)/4).*n.^-3+0.0625.*n.^-4;
% h2 = n2/d2;


% c)
% n2 is the value numerator coefficients and d2 are the denominator coefficients of the rational transfer function
n2 = [0, 0.25, 0, -0.0625];
d2  = [1, -sqrt(3), 1.25, -sqrt(3)/4, 0.0625];
delta = [1, zeros(1, length(n)-1)];

% the impulse response of h
h2 = filter(n2,d2, delta);

%d) plot both responses
figure('Name', 'Q1(d): impulse response comparison');
stem(n, h1,'bo-', 'LineWidth', 2.0);
hold on; 
stem(n, h2, 'rx--', 'LineWidth', 2.0);
hold off; 
xlabel('n');
ylabel('amplitude')
title('h_1[n] from the expression vs. h_2[n] from H(z)');

% Compare the differences in values between h1 and h2
fprintf('  %3d   %13.8f   %13.8f   %11.3e\n', [n; h1; h2; abs(h1-h2)]);
fprintf('\nMaximum absolute difference: %.3e\n', max(abs(h1 - h2)));
