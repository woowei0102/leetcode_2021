#include<stdio.h>
#include<string.h>

int strLCS(string a, string b) {

    int res = 0;
    for (int i = 0; i < a.size(); i++) {
        for (int j = 0; j < b.size(); j++) {
            if (a[i] == b[j]) {
                res++;

            }
            else {
                break;
            }

        }
    }

}

a b c d e f

a b c d e f