% Ece lab 1 
% Q1 

% a)
figure

% i)    
subplot(3,1,1)
x1 = -10 : 40;
x1_fig = -5.1 * sin(0.1* pi * x1 - 3 * pi /4) + 1.1 * (0.4* pi*x1);
stem(x1_fig);

% ii)
x2 = 0 : 100;
x2_fig = ((-0.9).^x2) .* exp(1).^((1i * pi * x2)/10);

subplot(3,1,2)
stem(imag(x2_fig))

subplot(3,1,3)
stem(real(x2_fig))