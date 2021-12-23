#include<stdio.h>
#include<string.h>
#include<vector>

void stradd(char *str1, char *str2) {
    int l1 = strlen(str1) - 1;
    int l2 = strlen(str2) - 1;
    int carry = 0;
    vector<char> res;
    int op1, op2;
    while (l1 >= 0 || l2 >= 0) {
        if (l1 >= 0) {
            op1 = (str[l1] - '0');
        } else {
            op1 = 0;
        }
        if (l2 >= 0) {
            op2 = (str[l2] - '0');
        } else {
            op2 = 0;
        }

        carry = op1 + op2 + carry;
        res.insert(0, (carry % 10) + '0'); 
        carry =  carry / 10;
        l1--;
        l2--;

    }
    if (carry != 0)
        res.insert(0, '1');
    return res;
}

123
234
  7