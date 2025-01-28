#include <stdio.h>

int main() {
    int n;
    // Read input integer from stdin
    scanf("%d", &n);

    for (int i=1; i <= n; i++){

	


        if (n/i == 0){
            printf("%d", i);
        }
	else if ((n%i) == 0 && i == n){
	    printf("%d", i);	
	}
        else if((n%i) == 0){
            printf("%d ", i);
        }
    }

    printf("\n");
    return 0;
}
