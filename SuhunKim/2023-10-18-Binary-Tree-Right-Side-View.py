# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        li = []
        def helper(node, depth):
            if not node: return;
            if len(li) <= depth:
                li.append(0)
            li[depth] = node.val
            helper(node.left, depth+1)
            helper(node.right, depth+1)
            
        helper(root, 0)
        return li