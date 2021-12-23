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
class Solution {
public:
    bool isSymmertic(TreeNode* root) {
        if (root == NULL) return true;
        return mirrorVisit(root->left, root->right);
    }

    bool mirrorVisit(TreeNode* left, TreeNode* right) {
        if (left == NULL and right == NULL) return true;
        if (left == NULL or right == NULL) return false;
        if (left->val != right->val) return false;
        return mirrorVisit(left->left, right->right) and
                mirrorVisit(left->right, right->left);
    }
};
