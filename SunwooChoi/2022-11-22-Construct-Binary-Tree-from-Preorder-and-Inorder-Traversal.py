# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        assert(len(preorder) == len(inorder), "Two list must have same lengths")
        
        # the end of traversal
        if len(preorder) == 0:
            return None
        
        node = TreeNode(preorder[0])
        # find the index of root in inorder list
        split_pt = inorder.index(node.val)
        # split inorder for left and right children
        inorder_left, inorder_right = inorder[:split_pt], inorder[split_pt+1:]
        # split preorder for left and right chiddren
        preorder_left, preorder_right = preorder[1:len(inorder_left)+1], preorder[len(inorder_left)+1:]
        
        # recursively build left and right nodes
        node.left = self.buildTree(preorder_left, inorder_left)
        node.right = self.buildTree(preorder_right, inorder_right)
        
        return node
    
