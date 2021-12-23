#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string reverseWords(string str) {
        reverse(str.begin(), str.end());
        for (int i = 0, j = 0; i < str.size(); i = j + 1) {
            for (j = i; j < str.size(); ++j) {
                if (str[j] == ' ') break;
            }
            reverse(str.begin() + i, str.begin() + j);
        }
        return str;
    }
};

int main(){
    Solution s;
    cout << s.reverseWords("who am I") << endl;
}
