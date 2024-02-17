# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
       
       # base
        if not root:
           return root
       # find tarket node
        if root.val > key:
        # go to the left
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
        # go to the right
            root.right = self.deleteNode(root.right, key)
       # If you find a target node, check condition
        else:
            # does node have only right node?
            if not root.left:
                return root.right
            # does node have only left node?
            elif not root.right:
                return root.left
            # does node have both?
            # go to the right node and find minimum value
            current = root.right
            while current.left:
                current = current.left
            # assign that minimun value to current target node's value
            root.val = current.val
            # remove the node contains minimum value
            root.right = self.deleteNode(root.right, root.val)
            # Because binary tree should assign larger value to the right and smaller value to the left
        return root