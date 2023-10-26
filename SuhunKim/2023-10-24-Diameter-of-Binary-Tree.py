# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        distance = []
        def checkDepth(node, depth):
            if not node: return depth
            leftDepth = checkDepth(node.left, depth+1)
            rightDepth = checkDepth(node.right, depth+1)
            if leftDepth and rightDepth:
                distance.append(leftDepth+rightDepth-(depth+1)*2)
            return max(leftDepth, rightDepth)
        
        checkDepth(root, 0)
        return max(distance)