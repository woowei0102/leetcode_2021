#include <stdio.h>

void swap(int *a, int *b) {
    int *tmp = a;
    a = b;
    b = tmp;
}

int main() {
    int x = 3, y = 2;
    printf("%d %d\n", x, y);
    swap(&x, &y);
    printf("%d %d\n", x, y);
}