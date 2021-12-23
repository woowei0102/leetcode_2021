#include <stdio.h>
#include <stdlib.h>

int setBit (int a, int b) {
    return a |= (0x1 << (b - 1));   
}

int clearBit (int a, int b) {
    return a &= ~(0x1 << (b - 1));   
}

int reverseBit (int a, int b) {
    return a ^= (0x1 << (b - 1));   
}


int main() {
    printf("%d\n", setBit(5, 2));
    printf("%d\n", clearBit(7, 2));
    printf("%d\n", reverseBit(7, 2));
}