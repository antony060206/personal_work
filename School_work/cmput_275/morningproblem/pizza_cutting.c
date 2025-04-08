#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

int main (){
    int slices = 0;
    int base = 0;
    int maximum = 1000000;
    scanf("%d %d", &base, &slices);

    int power_count = 0;
    int temp_next_base = 0;
    int temp_base = 0;
    while(true){
        temp_base = base;
        temp_next_base = base * base;

        if (slices > maximum){
            printf("BAD\n");
            break;
        }
        
        if(base == slices){
            printf("GOOOD\n");
            break;
        }
        else if (base < slices && slices < temp_next_base){
            printf("BAD\n");
            break;
        }
        
        base *= temp_base;

    }
    return 0;

    
}