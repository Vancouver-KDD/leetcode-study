# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Constraints:
# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1. first consider all the base cases
#    if both null, return true / if one null, return false / if the value is not the same, return False
# 2. recursively call the function on both the left and the right nodes on the tree
#    if they both return True after iterating over all nodes, the trees are the same, else False

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))