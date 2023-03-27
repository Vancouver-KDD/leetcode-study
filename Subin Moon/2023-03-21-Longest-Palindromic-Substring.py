"""
Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        longest_start_idx, longest_len = 0, 1

        for i in range(0, length):
            right = i
            while right < length and s[i] == s[right]:
                right += 1

            left = i - 1
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1

            pal_length = right - left - 1
            if pal_length > longest_len:
                longest_len = pal_length
                longest_start_idx = left + 1

        return s[longest_start_idx:longest_start_idx + longest_len]

    def longestPalindrome_2(self, s):
        res = ""
        res_len = 0

        # Go through every single position
        for i in range(len(s)):
            # odd length
            l, r = i, i  # centre position
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1

        return res