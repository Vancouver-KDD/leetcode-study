# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ret = 0
        def dfs(node, val):
            nonlocal ret
            if node.val >= val:
                val = node.val
                ret += 1
            if node.left:
                dfs(node.left, val)
            if node.right:
                dfs(node.right, val)
        dfs(root, root.val)
        return ret
