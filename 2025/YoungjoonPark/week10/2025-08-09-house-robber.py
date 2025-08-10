# KDD LeetCode Study Week 10: Dynamic Programming
# Assignment 1
# Author: Youngjoon Park
# URL: https://leetcode.com/problems/house-robber

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            current = max(nums[i] + prev2, prev1)
            
            prev2 = prev1
            prev1 = current
        
        return prev1