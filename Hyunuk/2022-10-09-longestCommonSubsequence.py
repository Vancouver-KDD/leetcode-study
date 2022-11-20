class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        r, c = len(text1), len(text2)
        dp = [[0] * (c + 1) for _ in range(r+1)]
        for x in reversed(range(c)):
            for y in reversed(range(r)):
                if text2[x] == text1[y]:
                    dp[y][x] = 1 + dp[y+1][x+1]
                else:
                    dp[y][x] = max(dp[y+1][x], dp[y][x+1])
        return dp[0][0]
