#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int Roman_num (char letter){
    switch (letter){
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
        default:
        printf("Invalid Roman numeral: %c\n", letter);
            return 0;  
        
    }
      
}

 int calculate (char *Arr, int size){
    int sum = 0;
    for (int i = 0; i < size; ++i){
        if(i==0){
            if (size == 1){
                sum += Roman_num(Arr[i]);
            }
            else if (Roman_num(Arr[i]) < Roman_num(Arr[i+1])){
                sum -= Roman_num(Arr[i]);
            }
            else{
                sum += Roman_num(Arr[i]);
            }
        }
        else if (i == size - 1 && size != 1){
            if(Roman_num(Arr[i]) >= Roman_num(Arr[i-1])){
                sum += Roman_num(Arr[i]);
            }
            else{
                sum -= Roman_num(Arr[i]);
            }
        }
        else{
            if(Roman_num(Arr[i]) >= Roman_num(Arr[i+1])){
                sum += Roman_num(Arr[i]);
            }
            else{
                sum -= Roman_num(Arr[i]);
            }
        }
    }
    return sum;
 }




 int main() {
    int capacity = 4;
    char *Roman = malloc(sizeof(char) * capacity);

    if (!fgets(Roman, capacity, stdin)) {
        free(Roman);
        return 1;
    }

    
    while (!strchr(Roman, '\n')) {
        capacity *= 2;
        Roman = realloc(Roman, capacity);
        if (!fgets(Roman + strlen(Roman), capacity / 2, stdin)) {
            break;
        }
    }

    Roman[strcspn(Roman, "\n")] = '\0';

    int value = calculate(Roman, strlen(Roman));
    printf("%d\n", value);
    free(Roman);
    return 0;
}
