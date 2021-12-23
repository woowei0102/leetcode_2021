class Solution():
    def preorderTraversal(self, root):
        res = []
        def preorder(root):
            if root is not None:
                print(root.val)
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)
            return res
        return preorder(root)

if __name__ == '__main__':
    s = Solution()
    print(s.preorderTraversal([1, None, 2, 3]))