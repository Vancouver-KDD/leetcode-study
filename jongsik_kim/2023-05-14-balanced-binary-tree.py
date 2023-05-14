from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return max(get_depth(node.left), get_depth(node.right)) + 1
        if not root:
            return True
        return abs(get_depth(root.left) - get_depth(root.right)) <= 1

