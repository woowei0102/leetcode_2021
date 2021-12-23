#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string word;
        if (strs.size() <= 0) return word;
        for (int i = 0; i <= strs[0].size(); i++){
            string w = strs[0].substr(0, i);
            // cout << i << ": " << w << endl;
            bool match = true;
            for (int j = 1; j < strs.size(); j++){
                if (i > strs[j].size() || w != strs[j].substr(0, i)){
                    match = false;
                    break;
                }
            }
            if (!match){
                return word;
            }
            word = w;
        }
        return word;
    }
};

int main(){
    Solution s;
    const char* t[] = {"abab", "aba", "abc"};
    vector<string> v(t, t+3);
    cout << s.longestCommonPrefix(v) << endl;
}