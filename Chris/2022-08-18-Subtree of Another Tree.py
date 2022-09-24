# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSametree(p, q):
            if p == None and q == None:
                return True
            if p == None or q == None:
                return False
            
            return p.val == q.val and isSametree(p.left,q.left) and isSametree(p.right, q.right)
        
        if subRoot == None:
            return True
        if root == None:
            return False
            
        if root.val == subRoot.val:
            return isSametree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)