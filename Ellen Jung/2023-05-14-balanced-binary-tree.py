# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        left = self.get_height(root.left)
        right = self.get_height(root.right)

        if abs(left - right) > 1:
            return False

        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)

        if left_balanced and right_balanced:
            return True
        else:
            return False

    def get_height(self, root):
        if root is None:
            return 0

        left_length = self.get_height(root.left)
        right_length = self.get_height(root.right)

        if left_length > right_length:
            return left_length + 1
        else:
            return right_length + 1