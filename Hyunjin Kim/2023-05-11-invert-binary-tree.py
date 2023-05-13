from typing import Optional
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #go to the right side first and print. if there isn't any,
        if not root :
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root
