# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        left_length = self.maxDepth(root.left)
        right_length = self.maxDepth(root.right)

        if left_length > right_length:
            return left_length + 1
        else:
            return right_length + 1
