# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        arr = []
        
        def inorder_bst(node):
            
            if node == None:
                return
            
            inorder_bst(node.left)
            arr.append(node.val)
            inorder_bst(node.right)
            
        inorder_bst(root)
        
        return arr[k-1]