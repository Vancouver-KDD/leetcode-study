# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def dfs(lo, hi):
            if hi < lo:
                return None

            last_po_value = postorder[self.po_index]

            curr = TreeNode(last_po_value)
            mid_index = in_order_map[last_po_value]

            self.po_index -= 1
            curr.right = dfs(mid_index + 1, hi)
            curr.left = dfs(lo, mid_index - 1)
            return curr

        self.po_index = len(postorder) - 1
        in_order_map = {}
        for i, val in enumerate(inorder):
            in_order_map[val] = i

        return dfs(0, len(postorder) - 1)