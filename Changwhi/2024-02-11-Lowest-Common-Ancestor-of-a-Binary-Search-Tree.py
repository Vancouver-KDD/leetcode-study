# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        sm, lg = p.val, q.val
        
        if sm > lg:
            sm, lg = q.val, p.val

        while True:
            if sm < root.val < lg or root.val == sm or root.val == lg:
                return root
            
            elif root.val > lg:
                root = root.left
            elif root.val < sm:
                root = root.right
                
            
                
            