#include <stdio.h>
#include <stdlib.h>

struct node {
        int a;
        long b, c;
        char d;
    };

int main() {
    printf("%lu\n", sizeof(struct node));
}