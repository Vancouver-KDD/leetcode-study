# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node, depth):
            if not node:
                return depth
            right = helper(node.right, depth + 1)
            left = helper(node.left, depth + 1)
            return max(right, left)
        return helper(root, 0)
