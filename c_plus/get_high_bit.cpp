#include<iostream>
using namespace std;

int f(unsigned char x){
    int n = 7;
    if (x == 0) return -1;
    if ((x >> 4) == 0){
        n = n - 4;
        x = x << 4;
        cout << 'a' << endl;
        // printf("%x\n", x);
    }
    
    if ((x >> 6) == 0) {
        n = n - 2;
        x = x << 2;
        cout << 'b' << endl;
    }
    if ((x >> 7) == 0) {
        n = n - 1;
        cout << 'c' << endl;
    }
    return n;
}

int main () {
    cout << f(0x40) << endl;
    // 0000 0001
    // 7654 3210
    // // 0010 0000
    // 1. n = 
    unsigned char a = 0x40;
    a >>= 6;
    printf("%x\n", a);
}

