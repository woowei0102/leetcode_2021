#include <stdio.h>

int bitcount(int n) {
    if (n > 0) {
        if (n & 1) return 1 + bitcount(n >> 1);
        else return bitcount(n >> 1);
    }
    return 0;
}

int main() {
    printf("%d\n", bitcount(5));
}