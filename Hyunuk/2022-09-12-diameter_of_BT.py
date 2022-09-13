# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal ret
            left, right = 0, 0
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            ret = max(ret, left+right)
            return max(left, right) + 1
            
        ret = 0
        if root:
            dfs(root)
        return ret
