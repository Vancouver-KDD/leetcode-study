# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal ret
            if not node:
                return 0
            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)
            path = node.val + left + right
            ret = max(ret, path)
            return node.val + max(left, right)
        ret = float("-inf")
        helper(root)
        return ret
