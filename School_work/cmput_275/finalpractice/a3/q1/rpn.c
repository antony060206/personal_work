#include <string.h>
#include <stdlib.h>
#include <stdio.h>

struct Stack{
    int size;
    int top;
    int *arr;
};

void push( struct Stack *s1, int item){
    //printf("%d", item);
    if(s1->size - 1 == s1->top){
        s1->size *= 2;
        s1->arr = realloc(s1->arr, sizeof(int)*s1->size);
    }
    s1->arr[++s1->top] = item;
}

int pop(struct Stack *s1){
    if(s1->arr == NULL){
        return 0;
    }
    else{
        return s1 -> arr[s1->top--];
    }
}

int calculate(int numb1, int numb2, char op){
    switch (op){
        case 'p':
            return (numb1+numb2);
        case 's':
            return (numb1-numb2);
        case '*':
            return (numb1*numb2);
        case '/':
            return (numb1/numb2);
    }
    return 0;
}

int main(){
    struct Stack s1;
    s1.top = 0;
    s1.size = 4;
    s1.arr = malloc(sizeof(int)*s1.size);
    
    int sum = 0;
    char c;
    while((c = getchar()) != EOF){
        int numb1 = 0;
        int numb2 = 0;

        switch (c){
            case ' ':
                break;

            case '0':
            case '1':
            case '2':
            case '3':
            case '4':
            case '5':
            case '6':
            case '7':
            case '8':
            case '9':
                int num = c - '0';
                push(&s1, num);
                break;

            case 'p':
            case 's':
            case '*':
            case '/':
                numb2 = pop(&s1);
                numb1 = pop(&s1);
                //printf("%d\n", numb1);
                int temp = calculate(numb1, numb2, c);
                //printf("%d %d %d\n", temp, numb1,numb2);
                push(&s1, temp);
                break;
        }
    }

    if(s1.top != 0){
        for(int i = 1; i <= s1.top;i++){
            sum += s1.arr[i];
        }
    }

    free(s1.arr);
    printf("%d\n", sum);
    return 0;

}