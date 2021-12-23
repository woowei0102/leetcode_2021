#include <iostream>
#include <vector>
using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
/* method 1
class Solution {
public:
    vector<int> inorderTraversal(TreeNode *root) {
        vector<TreeNode*> stack;
        vector<int> v;
        
        while(stack.size()>0 || root!=NULL){
            if (root!=NULL){
                stack.push_back(root);
                root = root->left;
            }else{
                if (stack.size()>0) {
                    root = stack.back();
                    stack.pop_back();
                    v.push_back(root->val);
                    root = root->right;
                }
            }
        }
        return v;
    }
}; */
// method 2
class Solution {
public:
    vector<int> res;
    void inorder(TreeNode *root) {
    if (root == NULL) return;
    inorder(root->left);
    res.push_back(root->val);
    inorder(root->right);
}
    
    vector<int> inorderTraversal(TreeNode *root) {
        inorder(root);
        return res;
    }
};