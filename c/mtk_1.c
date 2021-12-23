#include <stdio.h>

int fun(int x){

   int count = 0 ;

   while(x){

      count++ ;

      x = x & (x-1) ;

   }

   return count ;

}

int main() {
    printf("%d %d %d\n",fun(456), fun(123), fun(768));
    return 0;
}