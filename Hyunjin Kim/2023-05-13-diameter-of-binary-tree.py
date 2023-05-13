# Definition for a binary tree node.
from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def Length(root):
            if not root:
                return 0
            return max(Length(root.left), Length(root.right)) + 1

        if not root:
            return 0
        return max(self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right),
            Length(root.left) + Length(root.right))