# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Recursion -> pass node, string containing all ancesters
        # Concatenate this node value to the string
        # Check if it is leaf -> true append string to the result, false check left or right node

        result = []

        def travelTree(node, ancestors):
            if node:
                ancestors += str(node.val)
                if not node.left and not node.right:
                    # check if it is leaf
                    result.append(ancestors)
                else:
                    ancestors += "->"
                    travelTree(node.left, ancestors)
                    travelTree(node.right, ancestors)

        travelTree(root, "")

        return result
