from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = None

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # TRY_2: make a constant variable
        def helper(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_node = helper(node.left)
            right_node = helper(node.right)
            # store the diameter value
            self.diameter = max(self.diameter, left_node + right_node)
            # return the value of more deepest side
            return 1 + max(left_node, right_node)
        
        self.diameter = 0
        helper(root)
        return self.diameter

        # TRY_1
        # Failure - input: root = [1] / output: 1 / expected: 0
        # if not root:
        #     return 0
        # if not root.left and not root.right:
        #     return 1
        # left_diameter = self.diameterOfBinaryTree(root.left)
        # right_diameter = self.diameterOfBinaryTree(root.right)
        # return left_diameter + right_diameter


# class A:
#     def aa(self):
#         def b():
#             self.result = 1
#             print(self.result)
#         self.result = 0
#         print(self.result)
#         b()
#
#
# a = A()
# a.aa()
