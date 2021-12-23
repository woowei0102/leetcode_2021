#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        s = removeNoise(s);
        for (int i = 0; i < s.size() / 2; i++) {
            if (s[i] != s[s.size() - i - 1])
                return false;
        }
        return true;
    }

    string removeNoise(string& s){
        string d;
        for (int i = 0; i < s.size(); i++) {
            if (isalpha(s[i]) || isdigit(s[i])) {
                d.push_back(tolower(s[i]));
            }
        }
        return d;
    }
};

int main() {
    Solution s;
    cout << s.isPalindrome("A man, a plan, a canal: Panama") << endl;
}