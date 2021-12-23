#include <iostream>
using namespace std;

template<typename T, typename V>
T func(T a, V b)
{
    return a + b;
}

int main() {
	double i = 5.0;
	int j = 7;
	func(i, j);
	return 0;
}