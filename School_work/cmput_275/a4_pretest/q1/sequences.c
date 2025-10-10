#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

int process(char * buff, int size, int first_num){
    int sum = first_num;

    //printf("%d\n", sum);
    for (int i = 0; i < size; ++i){

        if(buff[i] == 'n'){
            buff[i] = ' ';
            break;
        }

        if (strncmp(&buff[i], "add", 3) == 0) {
            sum += buff[i + 4] - '0'; 
            //printf("%d\n", buff[i + 3]);
            i += 3; 
        } else if (strncmp(&buff[i], "sub", 3) == 0) {
            sum -= buff[i + 4] - '0'; 
            i += 3;
        } else if (strncmp(&buff[i], "mul", 3) == 0) {
            sum *= buff[i + 4] - '0'; 
            i += 3;
        } else if (strncmp(&buff[i], "div", 3) == 0) {
            if (buff[i + 4] != '0') {
                sum /= buff[i + 4] - '0';
            } else {
                printf("Error: Division by zero\n");
                return 0;
            }
            i += 3;
        } 
    }
    
    printf("%d\n", sum);
    return sum;
}


int main (int argc, char* argv[]){

    int capacity = 4;
    char *buff = malloc (sizeof(char)*capacity);
    char *all_lines = malloc(capacity * sizeof(char)); 

    if (argc < 2) {
        printf("Usage: %s <start_value>\n", argv[0]);
        free(buff);    // Add this
        free(all_lines); // Add this
        return 1;
    }
    int start_value = atoi(argv[1]);
    int next_value = start_value;

    *all_lines = '\0';  // Initialize the string to be empty

    while(1){
        // Read the next command
        if(!fgets(buff, capacity, stdin)){
            break;
        }

        // Check if the input line was truncated
        while (strchr(buff, '\n') == NULL) {
            // Double 
            capacity *= 2;
            buff = realloc(buff, sizeof(char) * capacity);
            if (!buff) {
                fprintf(stderr, "Memory reallocation failed\n");
                exit(1);
            }
            if (!fgets(buff + strlen(buff), capacity / 2, stdin)){
                break;
            }
        }


         // Remove the newline character if it exists
         size_t len = strlen(buff);

         if (len > 0 && buff[len - 1] == '\n') {
             buff[len - 1] = '\0';  // Remove the newline character
         }

         // Append the new line to the accumulated lines
         int new_len = strlen(all_lines) + strlen(buff) + 1;
         all_lines = realloc(all_lines, new_len * sizeof(char));
         if (all_lines == NULL) {
             fprintf(stderr, "Memory reallocation failed\n");
             return 1;
         }
         
        strcat(all_lines, buff);  

         int counter = 0;
        for (int i = 0; i < strlen(all_lines); ++i){
            if (all_lines[i] == 'n') { 
                counter++;
            }
            
        }

        for (int x = 0; x < counter; ++x){
            next_value = process(all_lines, strlen(all_lines), next_value);
        }

    }

    free(buff);
    free(all_lines);
    return 0;
}

