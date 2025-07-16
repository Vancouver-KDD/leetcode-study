# KDD LeetCode Study Week 7: Backtracking
# Assignment 3
# Author: Youngjoon Park
# URL: https://leetcode.com/problems/combination-sum

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])
                path.pop()
        
        backtrack(0, [], target)
        return result