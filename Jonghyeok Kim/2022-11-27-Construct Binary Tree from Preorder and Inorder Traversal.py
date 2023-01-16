# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build_tree(preorder, inorder):
            if len(preorder) == 0 and len(inorder) == 0:
                return
            inorder_head_index = inorder.index(preorder[0])
            head = TreeNode(preorder[0])
            head.left = build_tree(preorder[1:inorder_head_index+1], inorder[:inorder_head_index])
            head.right = build_tree(preorder[inorder_head_index+1:], inorder[inorder_head_index+1:])
            return head
        return build_tree(preorder, inorder)