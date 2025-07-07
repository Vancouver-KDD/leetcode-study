# KDD LeetCode Study Week 2: TwoPtr & SlideWin
# Assignment 2
# Title: Longest Repeating Character Replacement
# Author: Youngjoon Park
# Date: 2025-06-09
# URL: https://leetcode.com/problems/longest-repeating-character-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        result = 0
        char_count = {}
        most_frequent_count = 0
        
        for right in range(len(s)):
            current_char = s[right]
            char_count[current_char] = char_count.get(current_char, 0) + 1
            
            most_frequent_count = max(most_frequent_count, char_count[current_char])
            
            current_window_size = right - left + 1
            if current_window_size - most_frequent_count > k:
                char_count[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        return result