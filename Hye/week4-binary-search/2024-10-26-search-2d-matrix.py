"""
Search 2D Matrix
Solved 
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        The 1D index can be parsed into 2D row and col indices
        """
        rows = len(matrix)
        cols = len(matrix[0])
        size = rows * cols

        left, right = 0, size - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // cols
            col = mid % cols
            mid_num = matrix[row][col]
            if mid_num == target:
                return True
            elif mid_num > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
