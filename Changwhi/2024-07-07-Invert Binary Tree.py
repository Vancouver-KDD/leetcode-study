# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: 
        def traverse(root):
            if root == None:
                return
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp
        node = root
        traverse(node)
        return node