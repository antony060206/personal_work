#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct sets {
    int *elements;
    int size;
    int capacity;
};

// Function to resize the set when full
void resize_set(struct sets *set) {
    set->capacity *= 2; 
    set->elements = realloc(set->elements, sizeof(int) * set->capacity);
    if (!set->elements) {
        fprintf(stderr, "Memory reallocation failed\n");
        exit(1);
    }
}


void add_element (struct sets *set, int value){
    
    if(set->size == set->capacity-1){
        resize_set(set);
    }
    for (int i =0; i < set->size; ++i){
        if(set -> elements[i] ==value){
            return;
        }
    }
    set ->elements[set->size++] = value;
}


void remove_element (struct sets *set, int value){
    int index = -1;
    if(set->size == 0){
        return;
    }
    else{
        for (int i = 0; i < set -> size; ++i){
            if(set->elements[i] == value ){
                index = i ;
                break;
            }
        }

        if (index == -1) {
            return; // Value not found
        }

        for (int x = index; x < set -> size; ++x){
            set->elements[x] = set ->elements[x+1];
            }
        
        set->size--;
        }
 }

int comp(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}


void print_set(struct sets *set){
    if(set->size != 0){
    qsort(set->elements, set->size, sizeof(int), comp);

    for (int i = 0; i < set -> size; ++i){
        printf("%d", set->elements[i]);
        if (i != set->size - 1) {
            printf(" ");
        }
    }
    printf("\n");
}

}


void print_union(struct sets *setx, struct sets *sety) {
    struct sets *union_set = malloc(sizeof(struct sets)); 
    union_set->capacity = 4;
    union_set->size = 0;
    union_set->elements = malloc(sizeof(int) * union_set->capacity);  
    

    // Add elements from set x
    for (int i = 0; i < setx->size; i++) {
        add_element(union_set, setx->elements[i]);
    }

    // Add elements from set y
    for (int i = 0; i < sety->size; i++) {
        add_element(union_set, sety->elements[i]);
    }

    print_set(union_set);
    free(union_set->elements);
    free(union_set);
}

void print_intersection(struct sets *setx, struct sets*sety) {
    struct sets *intersection_set = malloc(sizeof(struct sets)); 
    intersection_set->capacity = 4;
    intersection_set->size = 0;
    intersection_set->elements = malloc(sizeof(int) * intersection_set->capacity);  

    // Find common elements and add to intersection set
    for (int i = 0; i < setx->size; i++) {
        for (int j = 0; j < sety->size; j++) {
            if (setx->elements[i] == sety->elements[j]) {
                add_element(intersection_set, setx->elements[i]);
                break;
            }
        }
    }

    print_set(intersection_set);
    free(intersection_set->elements);
    free(intersection_set);
}
 
int main() {
    struct sets *setx = malloc(sizeof(struct sets)); //declare x and y sets
    struct sets *sety = malloc(sizeof(struct sets));  
    setx->capacity = 4;
    sety->capacity = 4;
    setx->size = 0;
    sety->size = 0;
    setx->elements = malloc(sizeof(int) * setx->capacity);  
    sety->elements = malloc(sizeof(int) * sety->capacity);// Allocate memory for the stack array


    int capacity_of_command = 4;

    char *command = (char *)malloc(sizeof(char)*capacity_of_command);
    char operation[2] = {0};
    //printf("%d, %li", capacity_of_command, sizeof(command));
    while (1) {
        capacity_of_command = 4;
        // Read the next command
        if (!fgets(command, capacity_of_command, stdin)) {
            break;  
        }

        // Check if the input line was truncated
        while (strchr(command, '\n') == NULL) {
            // Double 
            capacity_of_command *= 2;
            command = realloc(command, sizeof(char) * capacity_of_command);
            if (!command) {
                fprintf(stderr, "Memory reallocation failed\n");
                exit(1);
            }

            if (!fgets(command + strlen(command), capacity_of_command / 2, stdin)) {
                break;
            }
        }

        for (int i =0; i< strlen(command)-1;++i){
            // printf("%c", command[i]);
            if(command[i] == 'a'|| command[i] == 'r' || command[i] == 'p' || command[i] == 'u' || command[i] == 'i'){
                // Ignore leading whitespace and check the command
                if (sscanf(command + i, " %c", operation) == 1) {
                
                if (strncmp(operation, "q", 1) == 0) {
                    return 0;  // Quit the program
                } else if (strncmp(operation, "a", 1) == 0 || strncmp(operation, "r", 1) == 0) {

                    char targ;//values 
                    int value;
                    if (sscanf(command + i, " %c %c %d", operation, &targ, &value) == 3) {
                        struct sets *set = (targ == 'x') ? setx : sety;

                        if (strncmp(operation, "a", 1) == 0) {
                            add_element(set, value);  // Add element
                        } else if (strncmp(operation, "r", 1) == 0) {
                            remove_element(set, value);  // Remove element
                        }   
                    }
                } else if (strncmp(operation, "p", 1) == 0) {
                    char targ;
                    if (sscanf(command + i, " %c %c", operation, &targ) == 2) {
                        struct sets *set = (targ == 'x') ? setx : sety;
                        print_set(set);  // Print set
                    }
                } else if (strncmp(operation, "u", 1) == 0) {
                    print_union(setx, sety);  // Print union
                } else if (strncmp(operation, "i", 1) == 0) {
                    print_intersection(setx, sety);  // Print intersection
                }
                }
            }
        }   

    }

    free(command);
    free(setx->elements);
    free(sety->elements);
    free(setx);
    free(sety);
    return 0;
}