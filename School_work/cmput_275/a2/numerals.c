#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int roman_conv(char c){
    switch (c){
        case 'I':
            return 1;
        case 'V':
            return 5;
        case 'X':
            return 10;
        case 'L': 
            return 50;
        case 'C':
            return 100;
        case 'D': 
            return 500;
        case 'M':
            return 1000;
        default: return 0;
    }
}


void convert(char numeral[], int size){

    int sum = 0;
    int current = 0;
    int next = 0;
    
    for (int i = 0; i < size; ++i){
        current = roman_conv(numeral[i]);

        if (i == size - 1){
            sum += current;
        }
        else{
            next = roman_conv(numeral[i+1]);
            if(current >= next){
                sum += current;
            }
            else{
                sum -= current;
            }
        }
    }

    printf("%d\n", sum);
}


int main (){
    char numeral[20];
    scanf("%24s", numeral);
    convert(numeral, strlen(numeral));
    return 0;
}