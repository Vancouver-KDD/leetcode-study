# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
                    return
        self.flatten(root.right)  # Recursively flatten the right subtree
        self.flatten(root.left)  # Recursively flatten the left subtree
        root.right = self.prev  # Set the right child to the previously flattened node
        root.left = None  # Set the left child to None
        self.prev = root  # Update the previously flattened node to be the current node
        