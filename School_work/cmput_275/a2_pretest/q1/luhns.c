#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int luhns_alg(int value) {
    int sum;
    int check_value;
    int dig_remove;
    int current_last;
    int power;
    check_value = value % 10;
    dig_remove = check_value;


    while(value){

        value = (value - dig_remove)/10;
        current_last = value % 10; 
        power += 1;

        //check if current value is odd digit or even
        if (power % 2 && power != 0){
            current_last = current_last*2;
            if(current_last >= 10){
                sum += current_last - 9;
            }
            else{
                sum += current_last; 
            }
        }
        else{
            sum += current_last;
        }
        
        dig_remove = current_last/2;
    }

    int final_result = (sum*9)%10;

    if (final_result == check_value){
        printf("Valid\n");

    }
    else{
        printf("Invalid\n");
    }

    //if final remainder is equal to the check value then valid other wise invalid 
    
}

int main() {
    int value;
    scanf("%d", &value);
    luhns_alg(value);

}