#Recursion => O((nm)^2) , space O(1)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 1:
                return 1 if text1[0] in text2 else 0
        
        if len(text2) == 1:
                return 1 if text2[0] in text1 else 0
            
            
        
        if text1[0] == text2[0]:
            return 1 + self.longestCommonSubsequence(text1[1:], text2[1:])
        else:
            return max(self.longestCommonSubsequence(text1, text2[1:]), self.longestCommonSubsequence(text1[1:], text2))




# 2-D DP => TC : O(nm) SC: O(nm)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        lcs = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                if text1[i] == text2[j]:
                    lcs[i][j] = 1 + lcs[i+1][j+1]
                else:
                    lcs[i][j] = max(lcs[i][j+1], lcs[i+1][j])
                    
        
        return lcs[0][0]
