# Definition for a binary tree node.
from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.height(root.left) + 1
        right = self.height(root.right) + 1

        return max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        left = self.height(root.left)
        right = self.height(root.right)

        if abs(left - right) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
