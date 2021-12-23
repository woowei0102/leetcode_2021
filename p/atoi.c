#include<stdio.h>

int atoi(char *s) {
    int i = 0;
    int res = 0;
    int isPositive = 1;

    while(s[i] == ' ')
        i++;
        
    if (s[i] == '-') {
        isPositive = -1;
        i++;
    }

    while(s[i] >= '0' && s[i] <= '9') {
        res = res * 10 + (s[i] - '0');
        i++;
    }

    return isPositive * res;
}