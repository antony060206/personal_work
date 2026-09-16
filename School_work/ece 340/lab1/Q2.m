%a)
% o hey o hey

% b)
[x3, Fs] = audioread('baila.wav');

% c)
num_samples = size(x3, 1);
t = (0 : num_samples - 1) / Fs;

figure
plot(t, x3)
xlabel('Time (s)')
ylabel('Amplitude')
title('baila.wav signal')

% e)
x3s = x3(1 : floor(num_samples / 2), :);

%f)
audiowrite('baila_half.wav', x3s, Fs);