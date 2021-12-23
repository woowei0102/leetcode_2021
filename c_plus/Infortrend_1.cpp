#include <iostream>
using namespace std;

int main() {
  
  int a = 129;
  char *b = (char*) &a;
  b[1] += 2;
  cout << a << endl;
}