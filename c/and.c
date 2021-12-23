#include <stdio.h>
#include <stdlib.h>

int divide3(int a){
    int ans = 0;
    while(a){
        ans += a&1;
        a>>=1;
        ans -= a&1;
        a>>=1;
    }
    return !(ans);
}

// 11
// 1001
// 11101
// 110011
// 32+16+8+4+2+1

int main(void) {
    int a = 5;
    printf("%d\n", divide3(27));
}