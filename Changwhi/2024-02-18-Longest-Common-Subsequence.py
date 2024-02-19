class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        2d dp
        bottom up
        
        """
        dp = [[0 for row in range(len(text1)+ 1)] for col in range(len(text2) + 1)] # extra column and row to set up the bottom value
        
        for row in range(len(text1) - 1, -1, -1): #start, stop, step 
            for col in range(len(text2) - 1, -1, -1):
                if text1[row] == text2[col]:
                    dp[col][row] = 1 + dp[col + 1][row + 1]
                else:
                    dp[col][row] = max(dp[col+1][row], dp[col][row+1])
        return dp[0][0]