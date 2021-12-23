#include<stdio.h>

int f_r(int a, int b) {
    if (b == 0)
        return a;
    else   
        return f_r(b, a % b);
}

int f_i(int a, int b) {
    int temp;
    while (b != 0) {
        temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

int main() {
    printf("%d\n", f_r(50, 10));
    printf("%d\n", f_i(50, 10));
}