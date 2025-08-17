# KDD LeetCode Study Week 11: Dynamic Pro
# Assignment 1
# Author: Youngjoon Park
# URL: https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, size = 0, 1

        for i in range(1, len(s)):
            l, r = i - size, i + 1
            window = s[l-1:r]

            if l >= 1 and window[::-1] == window:
                size += 2
                start = l - 1
            else:
                cur_window = s[l:r]
                if cur_window[::-1] == cur_window:
                    size += 1
                    start = l
        
        return s[start:start+size]