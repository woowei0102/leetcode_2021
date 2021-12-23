#include<iostream>
using namespace std;

int f(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return f(b, a % b);
    } 
}   

int main() {
    cout << f(100 , 40) << endl;
}