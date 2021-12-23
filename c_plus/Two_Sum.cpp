#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>  

using namespace std;
// method 1
// class Solution {
// public:
//     vector<int> twoSum(vector<int>& nums, int target) {
//         int begin = 0;
//         int end = nums.size() - 1;
//         int curr;
//         int nums_index[nums.size()][nums.size()];
//         vector<int> result;
//         for (int i = 0; i < nums.size(); i++) {
//             nums_index[i][0] = i;
//             nums_index[i][1] = nums[i];
//             // cout << nums_index[i]  << endl;
//         }


//         sort(nums.begin(), nums.end());

//         while (begin < end) {
//             curr = nums[begin] + nums[end];
//             if (curr == target) {
//                 // result.push_back(nums[begin]);
//                 // result.push_back(nums[end]);
//                 break;
//             }
//             else if (curr < target){
//                 begin += 1;
//             }
//             else {
//                 end -= 1;
//             }
//         }
//         int one, two;
//         one = -100;
//         for (int i = 0; i < nums.size(); i++) {
//             if ((nums_index[i][1] == nums[begin]) && (one == -100)){
//                 one = nums_index[i][0];
//             }
//             else if (nums_index[i][1] == nums[end]) {
//                 two = nums_index[i][0];
                
//             }
//         }
//         if (one > two) {
//             int temp = one;
//             one = two;
//             two = temp;
//         }
//         result.push_back(one);
//         result.push_back(two);
//         return result;
//     }
// };
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        /* method 2
        vector<int> result;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target){
                    result.push_back(i);
                    result.push_back(j);
                    break;
                }
                    
            }
        }
        return result;
        */
       // method 3
        unordered_map<int, int> m;
        vector<int> result;
        for (int i=0; i<nums.size(); i++) {
            // Searching for element (target - nums[i])
            if ( m.find(target - nums[i]) == m.begin() ) {
                // 沒有的話
                m[nums[i]] = i;
            }else{
                result.push_back(m[target - nums[i]]);
                result.push_back(i);
            }
        }
        return result;
    }
};

int main() {
    Solution s;
    vector<int> nums = {-1, -2, -3, -4, -5};
    int target = -8;
    vector<int> ans = s.twoSum(nums, target);
    cout << ans[0] << " " << ans[1] << endl;
}