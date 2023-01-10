class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        
        dp = [[float("inf")] * (len(word2)+1) for i in range(len(word1)+1)]
        
        for j in range(len2 +1):
            dp[len1][j] = len2 - j
        for i in range(len1 +1):
            dp[i][len2] = len1 - i
            
        for i in range(len1 -1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                #in case where current characters are equal
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    # compare all three cases and choose min
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j + 1], dp[i+1][j+1])
                    
        return dp[0][0]
        
            
        
        
        