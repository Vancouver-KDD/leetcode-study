# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root == None:
            return (subRoot == None)
        
        if subRoot == None:
            return True
        
        def sameTree(r, s):
        
            if r == None or s == None:
                return r == s
        
            if r.val == s.val:
                return sameTree(r.left, s.left) and sameTree(r.right, s.right)
            
            else:
                return False
        
        if root.val == subRoot.val:
            return sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
