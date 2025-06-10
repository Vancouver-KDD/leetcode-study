# KDD LeetCode Study Week 1: Array & Hashing
# Assignment 2
# Title: Two Sum
# Author: Youngjoon Park
# Date: 2025-06-05
# URL: https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]