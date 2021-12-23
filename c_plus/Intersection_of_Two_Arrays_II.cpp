#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        vector<int> res;
        int pos1 = 0;
        int pos2 = 0;
        while (pos1 < nums1.size() and pos2 < nums2.size()) {
            if (nums1[pos1] == nums2[pos2]) {
                res.push_back(nums1[pos1]);
                pos1++;
                pos2++;
            }
            else if (nums1[pos1] < nums2[pos2]) {
                pos1++;
            } else {
                pos2++;
            }
        }
        return res;
    }
};