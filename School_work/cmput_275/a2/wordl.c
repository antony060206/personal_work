#include <stdio.h>
#include <string.h>
const char * const GREEN = "\x1b[32m";
const char * const YELLOW = "\x1b[33m";
const char * const WHITE = "\x1b[0m";
const char * current = WHITE;

void setColour(const char *colour) {
  if (current == colour) return;
  printf("%s", colour);
  current = colour;
}

int printColoredGuess(char theWord[], char user_guess[], int size){
  

 // Find how many times each character in user_guess appears in theWord
 int wordCharCounts[12] = {0};  // Count occurrences in theWord
 int greenCounts[12] = {0};  // Track how many times we used green

 for (int i = 0; i < size; i++) {
   for (int j = 0; j < size; j++) {
     if (user_guess[i] == theWord[j]) {
       wordCharCounts[i]++;
     }
   }
 }

 for (int i = 0; i < size; i++) {
   if (theWord[i] == user_guess[i]) {
     greenCounts[i]++;
   }
 }


//print actual colored
  for (int i = 0; i < size; ++i){//user guess loop

     //Corret letter and position
    if (user_guess[i] == theWord[i]){
      setColour(GREEN);
      printf("%c", user_guess[i]);
      
      for (int j = 0; j < size; ++j){
        if(user_guess[i] == user_guess[j]){
          wordCharCounts[j]--;
        }
      }

    }else{//incorrect letter at poisiton i 
      
      if(!wordCharCounts[i]){
        setColour(WHITE);
        printf("%c", user_guess[i]);
      }
      else{
        setColour(YELLOW);
        printf("%c", user_guess[i]);

        for (int k = 0; k < size; ++k){
          if(user_guess[i] == user_guess[k] && wordCharCounts[k] > greenCounts[k]){
            wordCharCounts[k]--;
          }
        }

        
      }
    }
  }
  printf("\n");
  return 0;
}

int main(int argc, char **argv) {
  if (argc != 2) {
    printf("Usage: %s word\n", argv[0]);
    return 1;
  }
  // theWord is not a pointer to a string that stores the command line argument word that was provided.
  char *theWord = argv[1];
  char user_guess[12];
  int guess = 0;

  while(guess < 6){
    guess += 1;
    setColour(WHITE);
    printf("Enter guess: ");
    scanf("%s", user_guess);

    printColoredGuess(theWord, user_guess, (int)strlen(theWord));

    // if the user guess correctly
    if(strcmp(user_guess, theWord) == 0){
      setColour(WHITE);
      printf("Finished in %d guesses\n", guess);
      return 0;
    }
    else if (guess > 5){ //if the user did not guess correctly after 6 times
      setColour(WHITE);
      printf("Failed to guess the word: %s\n", theWord);
      
    }
  }
  return 0;

}