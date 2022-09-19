# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(node, sub):
            if not node and not sub:
                return True
            if not node or not sub:
                return False
            return node.val == sub.val and is_same_tree(node.left, sub.left) and is_same_tree(node.right, sub.right)
        
        if not root:
            return False
        if root.val == subRoot.val and is_same_tree(root, subRoot):
            return True
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right
