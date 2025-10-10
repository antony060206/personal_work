#include <stdlib.h>
#include <stdio.h> 
#include <string.h>

// Create a stack structure
struct Stack {
    int *array;
    int top;
    int capacity; 
};

// Function to initialize the stack
void init_stack(struct Stack *s, int initial_capacity) {
    s->array = malloc(sizeof(int) * initial_capacity); 
    s->top = -1; 
    s->capacity = initial_capacity; 
}

// Function to append to the stack (with reallocation if necessary)
void append_stack(struct Stack *s, int value) {
    if (s->top == s->capacity - 1) {
        
        s->capacity *= 2; 
        s->array = realloc(s->array, sizeof(int) * s->capacity); 
        if (s->array == NULL) {
            
            fprintf(stderr, "Memory allocation failed\n");
            exit(1);
        }
    }
    s->array[++s->top] = value; 
}

// Function to pop from the stack
int pop_stack(struct Stack *s) {
    if (s->top == -1) {
        
        fprintf(stderr, "Stack underflow\n");
        exit(1);
    }
    return s->array[s->top--]; 
}

int main() {
    struct Stack s1; // Declare the stack
    init_stack(&s1, 4); //initizalize dynamic arrays with 4

    char c;
    while ((c = getchar()) != EOF) {
        int val = 0;

        
        if (c == ' ' || c == '\t' || c == '\n') {
            continue;
        }

        
        if (c == 'p' || c == 's' || c == '*' || c == '/') {
            int popped1 = pop_stack(&s1);
            int popped2 = pop_stack(&s1);
            
            
            switch (c) {
                case 'p':
                    val = popped1 + popped2;
                    break;
                case 's':
                    val = popped2 - popped1;
                    break;
                case '*':
                    val = popped1 * popped2;
                    break;
                case '/':
                    if (popped1 == 0) {
                        fprintf(stderr, "Division by zero error\n");
                        exit(1);
                    }
                    val = popped2 / popped1;
                    break;
            }
            append_stack(&s1, val); 
        }
        
        else if (c >= '0' && c <= '9') {
            append_stack(&s1, c - '0');
        }
    }

    
    printf("%d\n", s1.array[s1.top]);

    
    free(s1.array);

    return 0;
}
