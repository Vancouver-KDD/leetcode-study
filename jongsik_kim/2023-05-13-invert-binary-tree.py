from typing import Optional
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Input: root = [2,1,3]
# Output: [2,3,1]

# Input: root = []
# Output: []


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
        else:
            return None
        # TRY_1 - recursive
        # Failure - [2, 3, null, 1]
        # if not root:
        #     return None
        # if not root.left and root.right:
        #     root.left = root.right
        #     root.right = None
        # if not root.right and root.left:
        #     root.right = root.left
        #     root.left = None
        # if root.left and root.right:
        #     temp_tree = root.left
        #     root.left = root.right
        #     root.right = temp_tree
        #
        #     left_tree = self.invertTree(root.left)
        #     right_tree = self.invertTree(root.right)
        #     root.left = right_tree
        #     root.right = left_tree
        # return root

