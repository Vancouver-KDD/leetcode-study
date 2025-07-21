# KDD LeetCode Study Week 7: Backtracking
# Assignment 1
# Author: Youngjoon Park
# URL: https://leetcode.com/problems/subsets

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start, path):
            result.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return result