% b) 
figure;

subplot(2,1,1)
x1 = 0 : 4;
stem(x1)
xlabel('k'); 
ylabel('x[k]');
title('x[k] = k,   0 \leq k \leq 4');
xlim([-1 5]); ylim([-1 5]);

subplot(2,1,2)
h1 = 0:3;
h1_fig = 2 - h1;
stem(h1, h1_fig);
xlabel('k'); 
ylabel('h[k]');
title('h[k] = 2 - k,   0 \leq k \leq 3');
xlim([-1 5]); ylim([-2 3]);

%c)
figure;
w = conv(x1, h1_fig);
k = 0:(length(w)-1);
stem(k, w);
xlabel('k'); 
ylabel('w[k]');
title('w[k] = x[k] * h[k]');
xlim([-1 8]); ylim([min(w)-2 max(w)+2]);

