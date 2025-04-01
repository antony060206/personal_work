#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

struct Pos {
    int x, y;
  };
  
  // The Maze structure, free for you to define
  // as you like in maze.c
  struct Maze{
    char **grid;
    int height;
    int width;
    int end;
    struct Pos start;
    struct Pos current;

  };

  // The readMaze function, you must define it in maze.c
  // The behaviour of this function is to read in a maze
  // from standard input. Reads the maze line by line until 
  // receiving an entirely empty line, at which point it 
  // considers the maze complete.
  // If it does not receive exactly one start tile and
  // at least one goal tile it returns NULL
  struct Maze *readMaze(){
    struct Maze *maze = calloc(1, sizeof(struct Maze));
    maze->grid = NULL;

    int length_line = 4;
    char *line = calloc(length_line, sizeof(char));

    if (!maze) return NULL;

    //loop through std in to find width and height as well as store 2d input in to a 2d array

    int num_start = 0;
    int num_end = 0;

    while(1){
        if(!fgets(line, length_line, stdin)){
            break;
        }
        else if (num_start == 1 && num_end == 1){
            break;
        }
        else if (strlen(line) == 1){
            break;
        }

        // Check if the input line was truncated
        while (strchr(line, '\n') == NULL) {
            // Double 
            length_line *= 2;
            line = realloc(line, sizeof(char) * length_line);
            if (!line) {
                fprintf(stderr, "Memory reallocation failed\n");
                exit(1);
            }
            if (!fgets(line + strlen(line), length_line / 2, stdin)){
                break;
            }
        }

        // Two pointers initially at the beginning
        int i = 0, j = 0;

        // Skip leading spaces
        while (line[i] == ' ') i++; 

        // Shift the characters of string to remove
  	    // leading spaces
        while ((line[j++] = line[i++]));



        // Allocate space for new row
        maze -> width = strlen(line)-1;
        maze->height++;
        maze->grid = realloc(maze->grid, maze->height * sizeof(char *));
        if (!maze->grid) {
            fprintf(stderr, "Memory allocation failed\n");
            exit(1);
        }

        maze->width = strlen(line);
        if (line[maze->width - 1] == '\n') { // Remove newline safely
        line[maze->width - 1] = '\0';
        maze->width--;  // Adjust width
        }

        maze->grid[maze->height - 1] = malloc(maze->width + 1); // +1 for '\0'
        if (!maze->grid[maze->height - 1]) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
        }

        strcpy(maze->grid[maze->height - 1], line);

        //checks for 1 S and one G
        for (int i = 0; i< maze->width; ++i){
            if(line[i] == 'S'){
                maze -> start.x = i;
                maze -> start.y = maze->height-1;
                maze -> current.x = maze -> start.x;
                maze -> current.y = maze -> start.y;
                num_start++;
            }
            else if (line[i] == 'G'){
                num_end++;
                break;
            }
        }
    }

    //printf("%d, %d",maze ->width ,maze -> height);
    free(line);

    if(num_end == 0 || num_start == 0){
        return NULL;
    }

    return maze;
}

//check if the next move is valid and return the amount of move
int check_tile(struct Maze* maze, int current_x, int current_y, int* teleported, int x_mov, int y_mov){
    int next_tile_x = current_x + x_mov;
    int next_tile_y = current_y + y_mov;
    int moves = 0;
    // printf("%d %d", next_tile_y, next_tile_x);
    if (next_tile_y < 0 || next_tile_y >= maze->height || next_tile_x < 0 || next_tile_x >= maze->width){//prevent moving out of edges
        //printf("%d %d", next_tile_y, next_tile_x);
        return 0;
    }

    switch(maze->grid[next_tile_y][next_tile_x]){

        case 'S'://back to start
            return 1;

        case 'G'://goal 
            maze->end = 1;
            return 1;

        case 'O'://open
            return 1;

        case 'X'://wall and edge
        //printf("wall");
            return 0;
        
        case '0'://teleport
        case '1':
        case '2':
        case '3':
        case '4':
        case '5':
        case '6':
        case '7':
        case '8':
        case '9':
            *teleported = 1;
            for (int i = 0; i < maze->height;i++) {
                for (int j = 0; j < maze->width; j++) {
                    if(maze->grid[i][j] == maze->grid[next_tile_y][next_tile_x] && i != (next_tile_y) && j != (next_tile_x)){
                        maze->current.x = j, maze->current.y = i;
                    }
                }
            }
            return 0;

        case 'I'://ice
            moves = check_tile(maze, next_tile_x, next_tile_y, teleported, x_mov, y_mov);
            if(*teleported == 0){
                return 1 + moves;
            }else{
                return 0;
            }
        
        default: // Undefined tile (Failsafe)
            return 0;

    }
  }

  // The makeMove function, you must define it in maze.c
  // The behaviour of the function is that it takes
  // a pointer to a Maze and a character that is
  // one of 'n', 'e', 's', or 'w' and moves the player
  // in the given direction and returns to the
  // caller the players new position. Unless the player
  // has reached the goal position, then it returns
  // the position (-1, -1).
  struct Pos makeMove(struct Maze* maze, char move){
    int current_x = maze->current.x;
    int current_y = maze->current.y;
    int teleported = 0;
    
    switch (move){
        case 'w':
            maze->current.x -= check_tile(maze, current_x,  current_y, &teleported, -1, 0);
            break;
        case 'e':
            maze->current.x += check_tile(maze, current_x,  current_y, &teleported, 1, 0);  
            break;
        case 'n':
            maze->current.y -= check_tile(maze, current_x, current_y, &teleported, 0, -1);
            break;
        case 's':
            maze->current.y += check_tile(maze, current_x,  current_y, &teleported, 0, 1);
            break;
    }
    //printf("%d %d", maze->current.y, maze->current.x);

    //check if it has reached end
    if (maze->end == 1){
        struct Pos end_pos;
        end_pos.x = -1;
        end_pos.y = -1;
        //printf("%d %d", maze->current.x, maze->current.y);
        return end_pos;
    }
    return maze->current;
    
  }


  // The reset function, you must define it in maze.c
  // The behaviour of this function is that it takes
  // a pointer to a Maze and resets the players position
  // to the original starting position
  void reset(struct Maze* maze){
        maze->current.x = maze->start.x;
        maze->current.y = maze->start.y;
  }
  
  
  // The printMaze function, you must define it in maze.c
  // The behaviour of this function is that it prints
  // the maze to the screen.
  void printMaze(struct Maze* maze){
    for (int x = 0; x < maze ->width+2; x++){
        printf("%c", '-');
    }
    printf("\n");
    //printf("%d, %d", maze->current.x, maze->current.y); test
    for (int i = 0; i < maze->height;i++) {
        printf("%c", '|'); // Left border
        for (int j = 0; j < maze->width; j++) {
            
            if(i == maze->current.y && j == maze->current.x){
                printf("%c", 'P'); //print player tile
            }
            else{
                printf("%c", maze->grid[i][j]); // Print the tile
            }
        }
        printf("%c\n", '|'); // Right border
    }

    for (int y = 0; y < maze->width+2; y++){
        printf("%c", '-');
    }
    printf("\n");

  }
  
  // Frees all memory associated with the given Maze
  // which was allocated by the readMaze function
  // including the Maze itself and returns NULL.
  struct Maze *destroyMaze(struct Maze* maze ){
    if (!maze) return NULL;

    // Free each row
    for (int i = 0; i < maze->height; i++) {
        free(maze->grid[i]);
    }
    free(maze->grid); // Free grid array
    free(maze); // Free maze structure
    return NULL;
}
  