#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define a struct for a pixel
typedef struct {
    int r, g, b;
} Pixel;


    // Function to apply sepia filter
void sepia_filter(Pixel *image, int width, int height) {
    for (int i = 0; i < width * height; i++) {
        int newR = (int)(image[i].r * 0.393 + image[i].g * 0.769 + image[i].b * 0.189);

        int newG = (int)(image[i].r * 0.349 + image[i].g * 0.686 + image[i].b * 0.168);
        
        int newB = (int)(image[i].r * 0.272 + image[i].g * 0.534 + image[i].b * 0.131);
        
        image[i].r = (newR > 255) ? 255 : newR;

        image[i].g = (newG > 255) ? 255 : newG;

        image[i].b = (newB > 255) ? 255 : newB;
    }
}
// Function to flip the image horizontally
void flip_image(Pixel *image, int width, int height) {
    for (int row = 0; row < height; row++) {
        for (int col = 0; col < width / 2; col++) {
            int left_index = row * width + col;
            int right_index = row * width + (width - 1 - col);
            
            // Swap pixels
            Pixel temp = image[left_index];
            image[left_index] = image[right_index];
            image[right_index] = temp;
        }
    }
}
// Function to print the PPM image to standard output
void print_ppm(Pixel *image, int width, int height) {
    printf("P3\n");
    printf("%d %d\n", width, height);
    printf("255\n");
    
    for (int i = 0; i < width * height; i++) {
        printf("%d %d %d ", image[i].r, image[i].g, image[i].b);
        if ((i + 1) % width == 0) {
            printf("\n");
        }
    }
}
// Function to read PPM image from standard input
void prepare_img(Pixel **image, int *width, int *height, int sepia, int flip) {
    char format[3];
    int max_val;
    
    // Read the header
    scanf("%s", format);
    scanf("%d %d", width, height);
    scanf("%d", &max_val);
    
    // Allocate memory for the image
    *image = (Pixel *)malloc((*width) * (*height) * sizeof(Pixel));

      
    // Read pixel data
    for (int i = 0; i < (*width) * (*height); i++) {
        scanf("%d %d %d", &(*image)[i].r, &(*image)[i].g, &(*image)[i].b);
    }

    if(sepia){
        sepia_filter(*image, *width, *height);
    }
    else if(flip){
        flip_image(*image, *width, *height);
    }
}
int main (int argc, char *argv[]){
    Pixel *Image = NULL;
    int flip =  0;
    int sepia = 0;
    int width = 0;
    int height = 0;

    for (int i =0; i < argc; ++i){
        if(strcmp(argv[i], "-f") == 0){
            flip = 1;
        }
        else if (strcmp(argv[i], "-s") == 0){
            sepia = 1;
        }
    }

    prepare_img(&Image, &width, &height, sepia, flip);
    print_ppm(Image, width, height);
    free(Image);
}