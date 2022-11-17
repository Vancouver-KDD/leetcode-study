# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.compareTree(p, q)
    
    # dfs to compare same position node of p and q
    def compareTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # p and q reached to None at the same time
        if not p and not q:
            return True
        
        # comparison to see current node is same
        if not p and q:
            return False
        if p and not q:
            return False
        if p.val != q.val:
            return False
        
        # return True if both child nodes are same, otherwise return False
        return self.compareTree(p.left, q.left) and self.compareTree(p.right, q.right)

