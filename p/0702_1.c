#include<stdio.h>
#include<stdlib.h>

// 1. What is *ptr and ptr value after Instruction below? 
int main() {
    
    // unsigned long *ptr = (unsigned long *)0x00550055; 
    // ptr+=0x00110011; // ptr = 0x00660066
    // *ptr = 0x12345678>>4; // *ptr = 0x01234567
    // *ptr |=0x10000000; // *ptr = 0x11234567
    // *ptr &=~0x00000001;  // *ptr = 0x11234566
    // printf("%lu\n", *ptr); // *ptr=? 
    // printf("%x\n", ptr); // ptr=? 

    unsigned long  *p = (unsigned long *) 0x00550055;
    printf("%08x\n", p);
    p += 0x00110011;
    printf("%08x\n", p);

    return 0;
}
