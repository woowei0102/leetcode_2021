#include <iostream>
using namespace std;

int main() {
    for (int i = 0; i < 5; i++) {
        for (int k = 0; k < i; k++)
            printf(" ");
        for (int j = 0; j < 9 - 2 * i; j++)
            printf("*");
        printf("\n");
    }
}