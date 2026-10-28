% Lab 3 - Question 2
%a) H1 (zero: - 1) (pole:1.25)  H2: (zero: -1) (pole: 0.8)

n1 = [2  2];
d1 = [1 -1.25];
n2 = [2  2];
d2 = [1 -0.80];
 
%(a) Pole-zero diagrams
[z1, p1, k1] = tf2zpk(n1, d1);
[z2, p2, k2] = tf2zpk(n2, d2);

figure;
subplot(1,2,1); zplane(z1, p1);
title('H_1(z):  pole at z = 1.25');
xlabel('Real'); 
ylabel('Imaginary');

subplot(1,2,2); 
zplane(z2, p2);
title('H_2(z):  pole at z = 0.80'); 
xlabel('Real'); 
ylabel('Imaginary');

%b) 0 < w < 2pi
w = linspace(0, 2*pi);
H1 = freqz(n1, d1, w);
H2 = freqz(n2, d2, w);

figure('Name', 'Q2(b): frequency response of H1');
subplot(2,1,1);
plot(w, abs(H1), 'LineWidth', 1.2);
xlim([0 2*pi]); 
xticklabels({'0','\pi/2','\pi','3\pi/2','2\pi'});
xlabel('\omega (rad/sample)');
ylabel('|H_1(e^{j\omega})|');
title('Magnitude response of H_1(z)');

subplot(2,1,2);
plot(w, angle(H1), 'LineWidth', 1.2); 
xlim([0 2*pi]); 
xticks(0:pi/2:2*pi);
xticklabels({'0','\pi/2','\pi','3\pi/2','2\pi'});
xlabel('\omega (rad/sample)'); 
ylabel('\angle H_1(e^{j\omega})  [rad]');
title('Phase response of H_1(z)');

figure('Name', 'Q2(b): frequency response of H2');
subplot(2,1,1);
plot(w, abs(H2), 'LineWidth', 1.2);
xlim([0 2*pi]); 
xticks(0:pi/2:2*pi);
xticklabels({'0','\pi/2','\pi','3\pi/2','2\pi'});
xlabel('\omega (rad/sample)'); 
ylabel('|H_2(e^{j\omega})|');
title('Magnitude response of H_2(z)');


subplot(2,1,2);
plot(w, angle(H2), 'LineWidth', 1.2);
xlim([0 2*pi]); 
xticks(0:pi/2:2*pi);
xticklabels({'0','\pi/2','\pi','3\pi/2','2\pi'});
xlabel('\omega (rad/sample)'); 
ylabel('\angle H_2(e^{j\omega})  [rad]');
title('Phase response of H_2(z)');

%c)
n  = 0:25;
d  = (n == 0);                                
h1 = -1.6*d + 3.6*(1.25).^n;
h2 = -2.5*d + 4.5*(0.80).^n;

delta  = [1, zeros(1, length(n)-1)];
h1_chk = filter(n1, d1, delta);
h2_chk = filter(n2, d2, delta);

figure('Name', 'Q2(c): impulse responses');
subplot(2,1,1);
stem(n, h1, 'bo-', 'LineWidth', 1.1, 'MarkerSize', 5); grid on;
xlabel('n'); ylabel('h_1[n]');
title('Impulse response of H_1(z)  -  grows without bound (unstable)');
subplot(2,1,2);
stem(n, h2, 'ro-', 'LineWidth', 1.1, 'MarkerSize', 5); grid on;
xlabel('n'); ylabel('h_2[n]');
title('Impulse response of H_2(z)  -  decays to zero (stable)');

fprintf('Sum |h1[n]| over 0..25 = %.4f\n', sum(abs(h1)));
fprintf('Sum |h2[n]| over 0..25 = %.4f\n', sum(abs(h2)));