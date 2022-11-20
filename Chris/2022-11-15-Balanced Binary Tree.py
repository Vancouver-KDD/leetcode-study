# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, node):
            if node == None:
                return -1
            return max(self.getHeight(node.left), self.getHeight(node.right)) + 1
    
    def isBalancedHelper(self, node)-> (bool, int):
        
        if not node:
            return True, -1
        
        isLeftBalanced, leftHeight = self.isBalancedHelper(node.left)
        if not isLeftBalanced:
            return False, 0
        
        isRightBalanced, rightHeight = self.isBalancedHelper(node.right)
        if not isRightBalanced:
            return False, 0
        
        return (abs(leftHeight - rightHeight) < 2, max(leftHeight, rightHeight)+1)
    
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        
        return self.isBalancedHelper(root)[0]
        
        
            
            