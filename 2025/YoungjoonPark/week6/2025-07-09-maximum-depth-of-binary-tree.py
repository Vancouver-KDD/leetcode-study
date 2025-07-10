# KDD LeetCode Study Week 6: Trees (DFS/BFS)
# Assignment 3
# Author: Youngjoon Park
# URL: https://leetcode.com/problems/maximum-depth-of-binary-tree

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1