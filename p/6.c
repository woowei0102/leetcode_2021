#include <stdio.h>

struct point {
  int x,y;  
};

int main() {
    struct point p1;
    struct point *pp;
    pp = &p1;
    pp->x = 3;
    (*pp).y = 4;
    p1.y = 2;
    printf("%d %d\n",p1.x, pp->y);
}