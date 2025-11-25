# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        curr_root_index = 0
        inorder_indices = {}
        for index, node in enumerate(inorder):
            inorder_indices[node] = index

        def buildTreeSub(left, right):
            nonlocal curr_root_index
            if left > right:
                return None
            root_value = preorder[curr_root_index]
            node = TreeNode(root_value)
            curr_root_index += 1

            node.left = buildTreeSub(left, inorder_indices[root_value] - 1)
            node.right = buildTreeSub(inorder_indices[root_value] + 1, right)
            return node

        return buildTreeSub(0, len(preorder) - 1)
