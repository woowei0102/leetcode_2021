#include <stdio.h>
#include <stdlib.h>

enum STATE{
    RUNNING = 49,
    STOPPED = 50,
    FAILED = 51,
    HIBERNATING = 52
};

int main(void) {
    int input1;

    printf("Please provide integer in range [1-4]: ");
    input1 = getchar();

    if (input1 == STOPPED) {
        printf("Machine is stopped\n");
    } else if (input1 == RUNNING) {
        printf("Machine is running\n");
    } else if (input1 == FAILED) {
        printf("Machine is in failed state\n");
    } else if (input1 == HIBERNATING) {
        printf("Machine is hibernated\n");
    }

    exit(EXIT_SUCCESS);
}