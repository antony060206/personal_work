#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>


#define MAX_A 1000
int main (){
    
    int S;
    int A;

    scanf("%d %d", &S, &A);
    int my_arr[MAX_A] = {0};
 
    for (int i =0; i < A; ++i){
        scanf("%d", &my_arr[i]);
    }

    bool visited[MAX_A] = {false};
    int addr = 0;
    
    while (true) {
        if (my_arr[addr] < 0) {
            printf("%d\n", my_arr[addr]);
            break;
        }

        if (visited[addr]) {
            printf("There was a cycle\n");
            break;
        }
        visited[addr] = true;

        int next_address = my_arr[addr];

        addr = next_address - S;

    }
    
    return 0;
}