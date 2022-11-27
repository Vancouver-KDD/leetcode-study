# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Check null cases    
        if not preorder or not inorder:
            return None
        
        # first node in preorder traversal is always the root of the tree
        # in inorder traversal, the nodes before the root are always 
        # the left children of the root
        # and the nodes after the root are always the right children of the root
        # in preorder, the nodes from index 1 to index mid are the left childeren
        # and the nodes from index mid+1 to the end are the right childeren
        # in each traversal, the structure is recursively constructed
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root