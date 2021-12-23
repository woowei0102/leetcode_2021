
#include <stdio.h>

int c;

int func(int n){
    c *= n;
    return n;
}

int main(void) {
	c = 1;
	int n = 2;
	func(func(func(func(func(func(func(func(n)))))))); //c = 256
	printf("c = %d", c); // 37
	return 0;
}