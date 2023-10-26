# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        numbers = []
        def helper(node, num):
            num += str(node.val)
            if not node.left and not node.right: 
                numbers.append(int(num))
                return;
            if node.left:
                helper(node.left, num)
            if node.right:
                helper(node.right, num)
            
        helper(root, "")
        return sum(numbers)