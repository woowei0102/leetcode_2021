#include <stdio.h>

char *strcat (const char *str1, const char *str2) {
    char *copy = (char *) str1;
    char *head = copy;
    while (*copy != '\0') copy++;
    while (*str2 != '\0') *copy++ = *str2++;
    *copy = '\0';
    return head;
}

int main() {
    char str1[] = "Hello ", str2[] = "World!";
    printf("%s\n", strcat(str1, str2));
}