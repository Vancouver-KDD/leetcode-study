#        1
#       / \
#      2   3
#     / \
#    4   5
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0  # i don't understand.

    def diameterOfBinaryTree(self, root):
        self.maxDepth(root)
        return self.res

    def maxDepth(self, root):
        if root is None:
            return 0
        left = 0
        right = 0
        if root.left:
            left = self.maxDepth(root.left)
        if root.right:
            right = self.maxDepth(root.right)
        self.res = max(self.res, left + right)
        return max(left, right) + 1


# I don't understand why it didn't work!
'''
class Solution:
    def diameterOfBinaryTree(self, root):
        self.maxDepth(root)
        self.res = 0
        return self.res

    def maxDepth(self, root):
        if root is None:
            return 0
        left = 0
        right = 0
        if root.left:
            left = self.maxDepth(root.left)
        if root.right:
            right = self.maxDepth(root.right)
        self.res = max(self.res, left + right + 1)
        return max(left, right) + 1
    
    
'''
