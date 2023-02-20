# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkValid(node, leftBoundary, rightBoundary):
            if (node == None):
                return True
            if (node.val > leftBoundary and node.val < rightBoundary):
                return checkValid(node.left, leftBoundary, node.val) and checkValid(node.right, node.val, rightBoundary)
            else:
                return False

        return checkValid(root, float("-inf"), float("inf"))