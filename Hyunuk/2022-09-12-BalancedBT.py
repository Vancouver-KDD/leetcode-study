# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node, depth):
            if not node:
                return depth-1
            if not node.left and not node.right:
                return depth
            return max(get_height(node.left, depth + 1), get_height(node.right, depth + 1))
        if not root:
            return True
        l, r = get_height(root.left, 0), get_height(root.right, 0)
        return abs(l-r) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
