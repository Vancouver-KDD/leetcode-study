# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None

        def dfs(node):
            if not node:
                return False
            nonlocal res

            left = dfs(node.left)
            right = dfs(node.right)
            curr = node == p or node == q

            if left + right + curr >= 2:
                res = node

            return left or right or curr

        dfs(root)

        return res
