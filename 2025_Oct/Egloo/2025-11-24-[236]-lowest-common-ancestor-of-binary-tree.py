# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        answer = [None]
        self.travel(root, p, q, answer)

        return answer[0]


    def travel(self, node, p, q, answer):
        if not node:
            return 0

        l = self.travel(node.left, p, q, answer)
        r = self.travel(node.right, p, q, answer)
        
        c = 1 if node in [p, q] else 0

        r = l + r + c
        if r == 2 and not answer[0]:
            answer[0] = node

        return  r