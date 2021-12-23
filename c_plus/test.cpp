#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>  

using namespace std;

int main() {
    
    unordered_map<int, int> m = {{0, 100}, {1, 200}, {2, 300}};
    cout << m.end()->first << endl;

    return 0;
}