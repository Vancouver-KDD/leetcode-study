# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #check if subtree is empty
        if not t:
            return True
        #check if tree is empty where subtree isn't
        if not s:
            return False

        #call helper fn
        if self.sameTree(s, t):
            return True

        #recursively check if t exists in left or right of tree
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    #helper function to check if tree and subtree are the exactly the same
    def sameTree(self, s, t):
        #check if both tree and subtree are empty
        if not s and not t:
            return True

        #recursively check if parent and childern nodes are the same
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)

        return False  