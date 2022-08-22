# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        
        if root == None:
            return res
        
        res.append([root.val])
        
        if root.left != None or root.right != None:
            left = self.levelOrder(root.left)
            right = self.levelOrder(root.right)
            
            length = min(len(left), len(right))
            for i in range(length):
                res.append(left[i]+right[i])
            if len(left) < len(right):
                res = res + right[length:]
            else:
                res = res + left[length:]
        
        return res