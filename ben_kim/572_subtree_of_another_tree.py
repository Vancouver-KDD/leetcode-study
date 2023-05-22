# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot return True # 1
        if not root and subRoot: return False # 2
        if self.isSameTree(root, subRoot): return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) # 3
    
    def isSameTree(self, t1, t2):

        if not t1 and not t2: return True
        if not t1 or not t2: return False
        if t1.val != t2.val: return False

        return self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right, t2.right)


# 1. None is the subtree of every nodes. 
# 2. If a subRoot has more nodes than the root, it cannot be a sub. 
# 3. If the current node is not equal, it is considered True if it appears in either the left or right branches.