# KDD LeetCode Study Week 1: Array & Hashing
# Assignment 3
# Title: Group Anagrams
# Author: Youngjoon Park
# Date: 2025-06-05
# URL: https://leetcode.com/problems/group-anagrams

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in data:
                data[key].append(s)
            else:
                data[key] = [s]
    
        return list(data.values())