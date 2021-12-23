#include <iostream>
#include <vector>
using namespace  std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 1;
        vector<int> res;
        while (digits.size() > 0) {
            int x = digits.back();
            digits.pop_back();
            x += carry;
            res.insert(res.begin(), x % 10);
            carry = x / 10;
            
        }
        if (carry > 0) 
            res.insert(res.begin(), 1);
        return res;
    }
};

void printVector(vector<int> &v) {
    cout << "{";
    for (int i = 0; i < v.size(); i++) {
        cout << v[i];
        if (i != v.size() - 1)
            cout << ", ";
    }
    cout << "}" << endl;
}

int main () {
    Solution s;
    vector<int> l = {1, 2, 3};
    vector<int> v = s.plusOne(l);
    printVector(v);
    return 0;
}