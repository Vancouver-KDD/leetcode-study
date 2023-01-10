# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, l = float("-inf"), r = float("inf")):
            return l < node.val < r and dfs(node.left, l, node.val) and dfs(node.right, node.val, r) if node else True
        return dfs(root)
