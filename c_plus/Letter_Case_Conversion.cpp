#include<iostream>
using namespace std;

int tolower(char c){
    return (c >= 'A' && c <= 'Z') ? c ^ 32 : c;
//  return (c >= 'A' && c <= 'Z') ? c ^ (1<<5) : c;
//  return (c >= 'A' && c <= 'Z') ? c ^ ' ' : c;
}

int main() {
    unsigned int a,b;
    for (b = 2; b >=0; b--) a++;
    cout << a << endl;
    // printf("%c\n", tolower('A'));
}