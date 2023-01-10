# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        
        def count_good_nodes(node, cur_max):
            if node == None:
                return
            nonlocal count
            if node.val >= cur_max:
                count += 1
                count_good_nodes(node.left, node.val)
                count_good_nodes(node.right, node.val)
            else:
                count_good_nodes(node.left, cur_max)
                count_good_nodes(node.right, cur_max)
                
        count_good_nodes(root, -float("inf"))
        
        return count