# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def subhelper(rt, sub):
            
            if not rt and not sub:
                return True

            if rt and sub and rt.val == sub.val:
                 return subhelper(rt.left, sub.left) and subhelper(rt.right,sub.right)
            else:
                return False
        
        if not root:
            return False

        res = False

        if root and subRoot and root.val == subRoot.val:
            res = subhelper(root,subRoot)

        
        return res or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)