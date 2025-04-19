#include <stdio.h>
#include <stdlib.h>

int main (){
    int arrlen = 0;
    int space = 0;
    
    scanf("%d %d", &arrlen, &space);

    int *arr = malloc(arrlen * sizeof(int));
    if (!arr) {
        printf("Memory allocation failed\n");
        return 1;
    }

    for (int i = 0; i < arrlen; i++) {
        scanf("%d", &arr[i]);
    }

    long long *prefix_product = (long long *)malloc((arrlen + 1) * sizeof(long long));
    long long *suffix_product = (long long *)malloc((arrlen + 1) * sizeof(long long));
    
    if (!prefix_product || !suffix_product) {
        printf("Memory allocation failed\n");
        free(arr);
        return 1;
    }
    
    prefix_product[0] = 1;
    for (int i = 0; i < arrlen; i++) {
        prefix_product[i + 1] = prefix_product[i] * (arr[i] == 0 ? 1 : arr[i]);
    }
    
    suffix_product[arrlen] = 1;
    for (int i = arrlen - 1; i >= 0; i--) {
        suffix_product[i] = suffix_product[i + 1] * (arr[i] == 0 ? 1 : arr[i]);
    }
    
    for (int i = 0; i < arrlen; i++) {
        int left_bound = (i - space < 0) ? 0 : i - space;
        int right_bound = (i + space + 1 >= arrlen) ? arrlen : i + space + 1;
        
        long long product = prefix_product[left_bound] * suffix_product[right_bound];
        
        if (left_bound == 0 && right_bound == arrlen) product = 0;
        
        printf("%lld ", product);
    }
    
    printf("\n");
    free(arr);
    free(prefix_product);
    free(suffix_product);
}