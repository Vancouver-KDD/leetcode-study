# KDD LeetCode Study Week 7: Backtracking
# Assignment 2
# Author: Youngjoon Park
# URL: https://leetcode.com/problems/permutations

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    used[i] = False
        
        backtrack([])
        return result