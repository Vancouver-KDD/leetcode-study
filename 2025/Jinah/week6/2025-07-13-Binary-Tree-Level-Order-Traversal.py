# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:  # type: ignore
        res = []

        if not root:
            return res

        q = collections.deque()
        q.append(root)

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(level)

        return res
        