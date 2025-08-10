# KDD LeetCode Study Week 10: Dynamic Programming
# Assignment 3
# Author: Youngjoon Park
# URL: https://leetcode.com/problems/climbing-stairs

from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev2 = 1
        prev1 = 2
        
        for _ in range(3, n + 1):
            current = prev1 + prev2
            
            prev2 = prev1
            prev1 = current
        
        return prev1