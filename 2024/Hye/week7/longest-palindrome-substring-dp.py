"""
다른 dp 문제들은 이미 main 에 merge 가 되어있습니다.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_index = 0
        max_length = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for left in range(n-1, -1, -1):
            for right in range(left, n):
                if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True
                    if max_length < (right - left + 1):
                        max_index = left
                        max_length = right - left + 1
        
        return s[max_index:max_index+max_length]
