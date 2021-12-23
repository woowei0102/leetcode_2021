#include <stdlib.h>
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> res;
        for (int i = 0; i < numRows; i++) {
            vector<int> vec;
            vec.push_back(1);
            for (int j = 1; j < i; j++) {
                vec.push_back(res[i - 1][j - 1] + res[i - 1][j]);
            }
            if (i != 0) vec.push_back(1);
            res.push_back(vec);
        }
        return res;
    }
};

int main() {
    Solution s;
    // cout << s.generate(5) << endl;
}