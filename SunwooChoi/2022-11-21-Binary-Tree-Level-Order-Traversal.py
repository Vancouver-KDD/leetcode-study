# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # find the depth
        depth = self.findDepth(root)
        # initialize list which contains same number of subarray with depth
        result = [[] for _ in range(depth)]
        # append node values to list
        self.appendNodes(root, 0, result)
        return result
    
    # find the maximum depth of tree
    def findDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        return max(self.findDepth(root.left), self.findDepth(root.right)) + 1
    
    # append node value in list
    def appendNodes(self, node: Optional[TreeNode], cur_depth: int, lst: List[List[int]]) -> None:
        if not node:
            return
        self.appendNodes(node.left, cur_depth+1, lst)
        lst[cur_depth].append(node.val)
        self.appendNodes(node.right, cur_depth+1, lst)

