#include <stdio.h>
#include <stdlib.h>

int main() {
    int p[] = {1, 2, 3, 4, 5};
    int *q = malloc(sizeof(p));
    for (int i = 0; i < sizeof(p) / sizeof(p[0]); i++)
        *(q + i) = p[i];
    for (int i = 0; i < sizeof(p) / sizeof(p[0]); i++)
        printf("%d\n", *q++);
}