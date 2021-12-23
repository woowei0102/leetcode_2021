# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        sum -= root.val
        if sum == 0 and root.left is None and root.right is None:
            return True
        left = self.hasPathSum(root.left, sum)
        right = self.hasPathSum(root.right, sum)
        return (left or right)
