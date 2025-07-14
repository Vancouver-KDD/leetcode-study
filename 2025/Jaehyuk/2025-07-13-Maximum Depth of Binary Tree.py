# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #can use dfs, and maybe bfs too
        ans = 0
        if not root:
            return ans
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
