# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        q = []
        result = []

        if root:
            q.append([0, root])

        while len(q) != 0:
            top     = q.pop(0)
            depth   = top[0]
            node    = top[1]
            
            if len(result) == depth:
                result.append([])
            result[depth].append(node.val)

            if node.left:
                q.append([depth+1, node.left])
            if node.right:
                q.append([depth+1, node.right])

        return result