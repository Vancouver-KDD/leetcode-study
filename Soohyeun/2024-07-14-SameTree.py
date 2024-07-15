# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursion fuction
        # check current node, left sub-tree, right sub-tree : all three are true -> return true
        # otherwise, return false

        def compare_tree(p, q):
            if not p and not q:
                return True
            if not q or not p or p.val != q.val:
                return False
            return compare_tree(p.left, q.left) and compare_tree(p.right, q.right)

        return compare_tree(p, q)
