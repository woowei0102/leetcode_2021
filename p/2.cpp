#include <iostream>

void even(){
    int res = 0;
    for (int i = 1; i <= 100; i++) {
        res += i;
        if (res % 2 == 0)
            printf("%d ",res);
    }    
    printf("\n");
}

void odd(){
    int res = 0;
    for (int i = 1; i <= 100; i++) {
        res += i;
        if (res % 2 != 0)
            printf("%d ",res);
    }    
    printf("\n");
}

int main() {
    even();
    odd();
}