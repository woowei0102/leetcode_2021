#include <iostream>

int main() {
    for (int i = 0; i < 3; i++) {
        for (int k = 0; k < i; k++)
            printf("  ");
        for (int j = 0; j < 5 - 2 * i; j++)
            printf("* ");
        printf("\n");
    }
}