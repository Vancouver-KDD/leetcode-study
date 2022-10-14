class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        if text1 == "" or None or text2 == "" or None:
            return 0
        
        else:
            if text1[-1] == text2[-1]:
                return (1 + self.longestCommonSubsequence(text1[:-1], text2[:-1]))
            else:
                return max(self.longestCommonSubsequence(text1[:-1], text2), self.longestCommonSubsequence(text1, text2[:-1]))