class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        for i in range(len(word2) + 1):
            for j in range(len(word1) + 1):
                if not i:
                    dp[i][j] = j
                elif not j:
                    dp[i][j] = i
                else:
                    if word2[i - 1] == word1[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
