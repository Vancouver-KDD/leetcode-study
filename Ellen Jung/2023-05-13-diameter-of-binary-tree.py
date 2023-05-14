# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.max = 0

    def getMax(self, root):

        if root is None:
            return 0

        left_length = self.getMax(root.left)
        right_length = self.getMax(root.right)

        if left_length + right_length > self.max:
            self.max = left_length + right_length

        return max(left_length, right_length) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        self.getMax(root)
        return self.max
