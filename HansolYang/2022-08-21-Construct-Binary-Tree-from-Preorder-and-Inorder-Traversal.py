# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        
        if preorder == None or len(preorder) == 0:
            return None
        
        root.val = preorder[0]
        i_root = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:i_root + 1], inorder[:i_root])
        root.right = self.buildTree(preorder[i_root+1:], inorder[i_root+1:])
        
        return root