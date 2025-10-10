#include <stdlib.h>
#include <stdio.h>

int main() {
    int number;
    scanf("%d", &number);
    printf("%d\n", number);

    int len_numb = 0;
    int int_temp = number;

    while (int_temp > 0) {
        int_temp = int_temp / 10;
        len_numb++;
    }

    int check = number % 10;
    number /= 10;  // remove check digit

    int sum = 0;
    int isSecond = 1; // every other digit from right to left

    for (int i = 0; i < len_numb - 1; ++i) {
        int digit = number % 10;
        number /= 10;

        if (isSecond) {
            digit *= 2;
            if (digit > 9) {
                digit -= 9;
            }
        }

        sum += digit;
        isSecond = !isSecond; // flip
    }

    sum *= 9;

    if ((sum % 10) != check) {
        printf("Invalid\n");
    } else {
        printf("Valid\n");
    }

    return 0;
}
