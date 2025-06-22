# KDD LeetCode Study Week 2: TwoPtr & SlideWin
# Assignment 1
# Title: Longest Substring Without Repeating Characters
# Author: Youngjoon Park
# Date: 2025-06-09
# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
    
        for i in range(0, len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                max_length = max(max_length, len(seen))
        
        return max_length






       