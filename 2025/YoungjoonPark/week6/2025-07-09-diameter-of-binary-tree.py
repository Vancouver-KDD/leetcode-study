# KDD LeetCode Study Week 6: Trees (DFS/BFS)
# Assignment 2
# Author: Youngjoon Park
# URL: https://leetcode.com/problems/diameter-of-binary-tree

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def get_height(node):
            if not node:
                return 0
            
            left_height = get_height(node.left)
            right_height = get_height(node.right)

            current_diameter = left_height + right_height

            self.max_diameter = max(self.max_diameter, current_diameter)

            return max(left_height, right_height) + 1
        
        get_height(root)
        
        return self.max_diameter