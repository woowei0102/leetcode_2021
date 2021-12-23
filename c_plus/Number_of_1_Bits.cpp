#include<iostream>
using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int cnt = 0;
        for (int i = 0; i < 32; i++) {
            if (n & 1) cnt++;
            n /= 2;
        }
        return cnt;

        int cnt = 0;
        for (int i = 0; i < 32; i++) {
            if (n & 1) cnt++;
            n >>= 1;
        }
        return cnt;
    }
};

int main() {
    Solution s;
    cout << s.hammingWeight(11) << endl;
}
