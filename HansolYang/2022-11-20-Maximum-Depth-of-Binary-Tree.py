# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        depth = 0
        
        if root:
            depth = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
        return depth
        