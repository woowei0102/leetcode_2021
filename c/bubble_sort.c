#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void bubble_sort(int *s) {

    for(int i = 0; i < 5; i++) {
        int f = 0;
        for (int j = 0; j < 5 - i - 1; j++) {
            if (s[j] > s[j + 1]){
                int temp = s[j];
                s[j] = s[j + 1];
                s[j + 1] = temp;
                f = 1;
            }
        }
        if (f == 0) break;
    }
}



int main() {
    int a[] = {6, 4, 3, 2, 1};
    bubble_sort(a);
    for (int i = 0; i < 5; i++)
        printf("%d ",a[i]);
    printf("\n");
        
    return 0;
}