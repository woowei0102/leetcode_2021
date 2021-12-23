#include<stdio.h>
#include<string.h>

#define max(a, b) ((a) > (b) ? (a) : (b))

int longestCommonSubsequence(char * text1, char * text2){
    int len1 = strlen(text1);
    int len2 = strlen(text2);
    int dp[len1 + 1][len2 + 1];   
    int result = 0;

    for (int i = 0; i <= len1; i++) {
        for (int j = 0; j <= len2; j++) {
            if (i == 0 || j == 0)
                dp[i][j] = 0;
            else if(text1[i - 1] == text2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
                //result = max(result, dp[i][j];)
            }
            else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                // dp[i][j] = 0;
            }
        }
    }
    return dp[len1][len2];
    
}

int main(){
    char a[] = "abcdefg";
    char b[] = "abcd";
    printf("%d\n", longestCommonSubsequence(a, b));
}

