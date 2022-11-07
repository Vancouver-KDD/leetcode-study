# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(l, r):
            nonlocal pre_i
            if l > r:
                return None
            node = TreeNode(preorder[pre_i])
            pre_i += 1
            m = hm[node.val]
            node.left = helper(l, m-1)
            node.right = helper(m + 1, r)
            return node
        
        hm = {v: i for i, v in enumerate(inorder)}
        pre_i = 0
        return helper(0, len(preorder) - 1)
