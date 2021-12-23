#include <stdio.h>
#include <stdlib.h>

void strcpy(char *s, char *t) {
   while((*s = *t) != '\0') {
       s++;
       t++;
   }
}


int main(){
    
    char *p = (char*) malloc (4);
    p = ;
    printf("%c\n", *p);
    free(p);
    printf("%c\n", *p);
    return 0;

}