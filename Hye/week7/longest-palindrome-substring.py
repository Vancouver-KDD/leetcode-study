"""
5. Longest Palindromic Substring / Medium

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        """
        We need to consider palindrome substring with even and odd length
        1. for each type, iterate through the pivot, and expand lefwards and rightwards
        2. update max length and max substring
        """
        max_odd_str = ""
        max_odd_length = 0
        max_even_str = ""
        max_even_length = 0

        size = len(s)

        for pivot in range(size):
            left, right = pivot, pivot
            while left >= 0 and right < size:
                if s[left] == s[right]:
                    substring = s[left:right + 1]
                    # palindrome
                    if max_odd_length < len(substring):
                        max_odd_length = len(substring)
                        max_odd_str = substring
                    left -= 1
                    right += 1
                else:
                    break
        
        for pivot in range(size - 1):
            left, right = pivot, pivot + 1
            while left >= 0 and right < size:
                if s[left] == s[right]:
                    # palindrome
                    substring = s[left:right + 1]
                    if max_even_length < len(substring):
                        max_even_length = len(substring)
                        max_even_str = substring
                    left -= 1
                    right += 1
                else:
                    break
        
        return max_even_str if max_even_length > max_odd_length else max_odd_str
