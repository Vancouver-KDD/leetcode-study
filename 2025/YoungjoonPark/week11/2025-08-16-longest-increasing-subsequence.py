# KDD LeetCode Study Week 11: Dynamic Pro
# Assignment 3
# Author: Youngjoon Park
# URL: https://leetcode.com/problems/longest-increasing-subsequence

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
