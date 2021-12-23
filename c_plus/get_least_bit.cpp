#include<iostream>
using namespace std;

int f(unsigned char x){

    return x & (-x);
}

int main () {
    cout << f(0x01) << endl;
    
}

