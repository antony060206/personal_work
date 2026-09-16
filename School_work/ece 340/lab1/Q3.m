% b)
vase = imread('vase.jpg');
rows = size(vase, 1);
columns = size(vase, 2);
max_pixel = max(vase(:));

% c)
vase_bright = vase + 30;

% d)
imwrite(vase_bright, 'vase_bright.jpg', 'jpg', 'Quality', 100);

% e) slightly brigher than the original