#include<stdio.h>

int fib_r(int n) {
    if (n == 1 || n == 2) 
        return 1;
    else 
        return fib_r(n - 1) + fib_r(n - 2);
}



int fib_i(int n) {
    int a = 1, b = 1;
    int temp;
    if (n == 1 || n == 2)
        return 1;
    for (int i = 3; i <= n; i++) {
        temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

int main() {
    printf("%d\n", fib_r(10));
    printf("%d\n", fib_i(10));
}