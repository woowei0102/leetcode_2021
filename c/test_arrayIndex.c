#include <stdio.h>
#include <string.h>

void f(char *p) {
    printf("%d\n", strlen(p));
}

int main() {
    short arr[] = {0x1, 0x3, 0x5, 0x7, 0x9, 0xB, 0xD};
    printf("%08x\n", *(int*)(arr + 4));
    printf("%08x\n", *(short*)(((int *)arr + 1)));
    
    char str[] = "Hello World!!";
    printf("%s\n", str);
    printf("%d\n", strlen(str));
    return 0;
}