class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[j][i] = 1 + dp[j+1][i+1]
                else:
                    dp[j][i] = max(dp[j][i+1], dp[j+1][i])
        
        return dp[0][0]