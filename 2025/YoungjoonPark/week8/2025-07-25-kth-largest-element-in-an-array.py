# KDD LeetCode Study Week 8: Heap / Priority Queue
# Assignment 1
# Author: Youngjoon Park
# URL: https://leetcode.com/problems/kth-largest-element-in-an-array

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        newArr = sorted(nums)
        return newArr[len(newArr) - k]