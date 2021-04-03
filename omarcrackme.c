#include <stdio.h>
#include <string.h>

int main(void) 
{ 
    char inPass[128]; 
    char password[] = "123456";
    printf("try a password: "); 
    scanf("%s", inPass);
    int result = strcmp(inPass, password);
    printf("\n");
    if(result == 0){
        printf("wow congratulations you guessed the most common password. is the average person really this stupid?");
    }
    else{
        printf("incorrect. Try again");
    }
    return 0; 
} 