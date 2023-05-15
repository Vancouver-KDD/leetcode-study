from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # TRY_2 - recursive, set all the possibilities
        if (not p and q) or (p and not q):
            return False
        if not p and not q:
            return True
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

        # TRY_1
        # Failure - comparing the different addresses
        # if p.left != q.left or p.right != q.right:
        #     return False
        # self.isSameTree(p.left, q.left)
        # self.isSameTree(p.right, q.right)
        # return True
