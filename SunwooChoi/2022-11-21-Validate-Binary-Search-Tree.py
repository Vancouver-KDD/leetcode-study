# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder_list = []
        # append elements in list
        self.inorderTraverseTree(root, inorder_list)
        
        # if it is not ascending order, return false otherwise continue
        for idx in range(1, len(inorder_list)):
            if inorder_list[idx-1] >= inorder_list[idx]:
                return False
    
        return True
    
    # traverse tree in in-order and append elements from the tree into list 
    def inorderTraverseTree(self, root: Optional[TreeNode], inorder_list: List[int]) -> None:
        if not root:
            return
        self.inorderTraverseTree(root.left, inorder_list)
        inorder_list.append(root.val)
        self.inorderTraverseTree(root.right, inorder_list)

