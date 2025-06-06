# KDD LeetCode Study Week 1: Array & Hashing
# Assignment 1
# Title: Top K Frequent Elements
# Author: Youngjoon Park
# Date: 2025-06-05
# URL: https://leetcode.com/problems/top-k-frequent-elements

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
    
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        
        
        freq_list = [(freq, num) for num, freq in freq_dict.items()]
        
        freq_list.sort(reverse=True)
        
        result = [num for freq, num in freq_list[:k]]
        
        return result