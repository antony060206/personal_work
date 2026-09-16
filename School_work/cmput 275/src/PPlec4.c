#include <stdio.h>

// void print_binary(int: num){ 
//     int num_zeros = 0 
//     for (i = 0; num <= 2**i; ++i){
//         num_zeros += 1;
//     }

//     for (x = 0; x < num_zeros; ++x){
//         if num < 2**num_zeros
//     }
    

//     printf(value)
// }

// int main (){
//     print_binary(5)
// }

int print_binary (unsigned int x){
    //complete next class

    if (x == 0){
        printf("0");
        return 0;
    }

    int CurPow = 1;
    while( CurPow <= x){
        CurPow - CurPow*2;
    }
    while (x > 0){
        if (CurPow <= x){
            printf("1");
            x = x-CurPow;
        }else{
            printf("0");
        }
    }
}

int main(){
    print_binary(5);
}