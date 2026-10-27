%a)
figure
 
n = 0 : 30;
Fs = 100;                % sampling rate, Hz
T = 1/Fs;
y1 = cos(20 * pi * n * T);    % x1(t) = cos(20*pi*t), 10 Hz  -> cos(0.2*pi*n)
y2 = cos (180 * pi * n * T);  % x2(t) = cos(180*pi*t), 90 Hz -> cos(1.8*pi*n)
                              % 90 Hz > Fs/2 = 50, so it aliases to 10 Hz
 
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
fs2 = 1000;              % 10x the rate, so both signals are now below Nyquist
t2 = 1/fs2;
n2 = 0 : 300;            % 301 samples at 1000 Hz = same 0.3 s window as part a
 
z1 = cos(20 * pi * n2 * t2);    % 10 Hz, correctly sampled
z2 = cos (180 * pi * n2 * t2);  % 90 Hz, correctly sampled
 
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
plot(n2/fs2, z1,'r-', n/Fs, y1, 'b+');   % divide by fs to put both on a
                                         % common time axis before overlaying
xlabel('n');
ylabel('y_1[n] and z_1[n]');
legend('z_1[n]', 'y_1[n]');              % y1 markers sit on the z1 curve
 
subplot(2,1,2);
plot(n2/fs2, z2, 'r-', n/Fs, y2, 'b+');
xlabel('n');
ylabel('y_2[n] and z_2[n]');
legend('z_2[n]', 'y_2[n]');              % y2 markers follow a 10 Hz alias,
                                         % not the 90 Hz z2 curve
 
% c) using c f3 = 10 + m(100) = 110hz
figure
 
n3 = 0 : 30;
Fs3 = 100;
T3 = 1/Fs3;
x3 = cos(220 * pi * n3 * T3);   % cos(2.2*pi*n) = cos(0.2*pi*n) = y1[n]
 
stem(n3, x3, 'bo', 'MarkerSize', 10);   % big circles so both series show,
hold on                                 % since the two are exactly equal
stem(n, y1, 'r*');
hold off
 
xlabel('n');
ylabel('y_1[n] and y_3[n]');
ylim([-1.2 1.2]);
legend('y_3[n]', 'y_1[n]');
title('y_1[n] = cos(2.2\pi*n)   from  x_1(t) = cos(220\pi*t),  f_s = 100 Hz');
