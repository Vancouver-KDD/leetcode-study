# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # base case where roots p and q are both empty; reached the end of tree
        if not p and not q:
            return True

        # check if either tree is empty or roots are different
        if not p or not q or p.val != q.val:
            return False

        # check on subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# T O(n) n: total num of nodes in tree
# S O(n) n: height of the tree, O(n) in worst case where tree is skewed so that it looks like a list.

