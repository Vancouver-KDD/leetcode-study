# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        idx = inorder.index(preorder.pop(0))
        node = TreeNode(inorder[idx])

        node.left = self.buildTree(preorder, inorder[:idx])
        node.right = self.buildTree(preorder, inorder[idx + 1:])

        return node


        ## TC: O(n) ??