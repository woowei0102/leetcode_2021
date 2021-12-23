#include<iostream>
#include<string>
using namespace std;

class Solution {
public:
    int titleToNumber(string columnTitle) {
        int res = 0;
        for (int i = 0; i < columnTitle.size(); i++) {
            res = res * 26 + (long)columnTitle[i] - 64;
        }
        return res;
    }
};

int main() {
    Solution s;
    cout << s.titleToNumber("AB") << endl;
}