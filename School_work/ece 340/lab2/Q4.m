%a) 
barbara = imread('barbaraLarge.jpg');

%b) 
figure
imshow(barbara), colorbar;

%c) 
resize_factor = [0.9, 0.7, 0.5];

images = cell(2, length(resize_factor));

for rf_index = 1:length(resize_factor)
    rf = resize_factor(rf_index);
    images{1, rf_index} = imresize(barbara, rf, 'nearest', 'Antialiasing', 0);
    images{2, rf_index} = imresize(barbara, rf, 'nearest', 'Antialiasing', 1);

end

% plot all six
figure;
for rf_index = 1:length(resize_factor)
    rf = resize_factor(rf_index);

    subplot(2, 3, rf_index);
    imshow(images{1, rf_index});
    title(sprintf('%.1f, antialiasing off', rf));

    subplot(2, 3, rf_index + 3);
    imshow(images{2, rf_index});
    title(sprintf('%.1f, antialiasing on', rf));
end