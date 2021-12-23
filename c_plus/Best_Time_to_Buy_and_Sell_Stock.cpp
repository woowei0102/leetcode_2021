#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int length = prices.size();
        if (length == 0) return 0;
        int max_profit = 0;
        int low = prices[0];
        for (int i = 1; i < length; i++) {
            if (low > prices[i]) {
                low = prices[i];
            } else {
                int temp = prices[i] - low;
                if (temp > max_profit) {
                    max_profit = temp;
                }
            }
        }
        return max_profit;
    }
};