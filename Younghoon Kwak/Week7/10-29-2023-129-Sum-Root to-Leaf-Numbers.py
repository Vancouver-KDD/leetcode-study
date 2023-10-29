# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def isLeaf(node):
            if node is None:
                return False
            elif node.left is None and node.right is None:
                return True
            return False
        lst = []
        def dfs(node, sum):
            if node is None:
                return 
            elif isLeaf(node):
                lst.append(10*sum+node.val)
            dfs(node.left, 10*sum+node.val)
            dfs(node.right, 10*sum+node.val)
        dfs(root, 0)
        return sum(lst)