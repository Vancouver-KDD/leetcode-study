class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

        res = (0, 0, 0)
        for end in range(1, len(s)):
            for start in range(end):
                if s[start] == s[end]:
                    if end - start == 1:
                        dp[end][start] = True
                    else:
                        dp[end][start] = dp[end - 1][start + 1]
                    if dp[end][start] and end - start > res[0]:
                        res = (end - start, start, end)
        return s[res[1]: res[2] + 1]