%b) 
figure

h1 = 0 : 50;
h1_fig = 0.3*sinc(0.3*(h1-25)).*(0.54-0.46*cos((2*pi*h1)/50));
stem(h1, h1_fig);
xlabel('k');
ylabel('h[k]');
title('h[k] =  0.3*sinc(0.3*(h1-25)).*(0.54-0.46*cos((2*pi*h1)/50))n   0 \leq k \leq 50')



%c) 
[x3, fs] = audioread('baila.wav');
w = conv(h1_fig, x3);
audiowrite('baila_filtered.wav', w, fs);
