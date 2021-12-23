#include <stdio.h>
int add(int a, int b) {
  return a+b;
}

int mult(int a, int b) {
  return a*b;
}

int main() {
  int (*op)(int, int);
  op = add;
  printf("op(3,5)=%d\n", op(3,5));
  op = mult;
  printf("op(3,5)=%d\n", op(3,5));
}