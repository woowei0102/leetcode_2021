
#include <stdio.h>

int c;

int func(int m, int* n){
    c += 1;
    m += c;
    *n += m;
    return m;
}

// c 1 y 13 x 6
// c 2 y 21 z 8 x 6

int main(void) {
	c = 0;
	int x = 5;
	int y = 7;
	int z;
	x = func(x, &y);
	z = func(x, &y);
    printf("x: %d\n", x);
    printf("y: %d\n", y);
    printf("z: %d\n", z);
    printf("c: %d\n", c);
	printf("sum of x, y, z, and c = %d\n", x + y + z + c); // 37
	return 0;
}