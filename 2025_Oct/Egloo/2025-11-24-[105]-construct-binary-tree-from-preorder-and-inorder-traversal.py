# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def __init__(self):
        self.index = 0
        self.iMap = {}
        self.preorder = []

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.index = 0
        self.iMap = {}
        self.preorder = preorder
        
        for idx, value in enumerate(inorder):
            self.iMap[value] = idx

        return self.build(0, len(inorder)-1)

    def build(self, start, end):
        if start > end:
            return None
        c_val = self.preorder[self.index]
        current = self.iMap[c_val]

        if not current in range(start, end+1):
            return None

        node = TreeNode(c_val)
        self.index += 1

        node.left = self.build(start, current-1)
        node.right = self.build(current + 1, end)
        
        return node
        