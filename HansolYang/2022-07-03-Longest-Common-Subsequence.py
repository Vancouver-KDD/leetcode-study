class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        common = {}
        isf = -1
        maximum = 0
        curr = 0
        
        for i in range(len(text1)):
            common[text1[i]] = 1
        
        for j in range(len(text2)):
            if (common.get(text2[j]) == 1):
                if (text1.index(text2[j]) > isf):
                    curr+= 1
                    maximum = max(curr, maximum)
                else:
                    curr = 1
                isf = text1.index(text2[j])
                common[text2[j]] = 0
        
        return maximum