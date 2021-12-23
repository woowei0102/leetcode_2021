#include <iostream>
#include <string>
#include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for (auto ch : s) {
            if (ch == '{' || ch == '[' || ch == '(') {
                st.push(ch);
            }else if (ch == '}' || ch == ']' || ch == ')') {
                if (st.empty()) return false;
                char top = st.top();
                if ((top == '{' && ch == '}') || (top == '[' && ch == ']') || (top == '(' && ch == ')')){
                    st.pop();
                }else {
                    return false;
                }
            }else {
                return false;
            }
        }
        return st.empty();
    }
};

int main(){
    Solution s;
    cout << s.isValid("()") << endl;
}