%a)
figure

n = 0 : 30;
Fs = 100;
T = 1/Fs;
y1 = cos(20 * pi * n * T);
y2 = cos (180 * pi * n * T);

subplot(2, 1, 1);
stem(n, y1);
xlabel('n'); 
ylabel('y_1[n]'); 
ylim([-1.2 1.2]);
title('y_1[n] = cos(0.2\pi*nn)   from  x_1(t) = cos(20\pi*t),  f_s = 100 Hz');

subplot(2, 1, 2);
stem(n, y2);
xlabel('n');
ylabel('y_2[n]'); 
ylim([-1.2 1.2]);
title('y_2[n] = cos(1.8\pi*n)   from  x_1(t) = cos(180\pi*t),  f_s = 100 Hz');

%b) 
fs2 = 1000;
t2 = 1/fs2;
n2 = 0 : 300;

z1 = cos(20 * pi * n2 * t2);
z2 = cos (180 * pi * n2 * t2);

figure
subplot(2,1,1);
stem(n2, z1, 'filled', 'MarkerSize', 2);
xlabel('n'); 
ylabel('z_1[n]'); 
ylim([-1.2 1.2]);
title('z_1[n] = cos(0.02\pi n),  f_s = 1000 Hz');

subplot(2,1,2);
stem(n2, z2, 'filled', 'MarkerSize', 2); 
xlabel('n'); 
ylabel('z_2[n]'); 
ylim([-1.2 1.2]);
title('z_2[n] = cos(0.18\pi n),  f_s = 1000 Hz');

figure

subplot(2,1,1);
plot(n2/fs2, z1,'r-', n/Fs, y1, 'b+');
xlabel('n');
ylabel('y_1[n] and z_1[n]');
legend('z_1[n]', 'y_1[n]');

subplot(2,1,2);
plot(n2/fs2, z2, 'r-', n/Fs, y2, 'b+');
xlabel('n');
ylabel('y_2[n] and z_2[n]');
legend('z_2[n]', 'y_2[n]');

% c) using c f3 = 10 + m(100) = 110hz
figure

n3 = 0 : 30;
Fs3 = 100;
T3 = 1/Fs;
x3 = cos(220 * pi * n * T3);

stem(n3, x3);
xlabel('n'); 
ylabel('y_3[n]'); 
ylim([-1.2 1.2]);
title('y_1[n] = cos(2.2\pi*nn)   from  x_1(t) = cos(220\pi*t),  f_s = 100 Hz');

