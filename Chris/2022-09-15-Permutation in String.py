class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:        
        def isPermutation(string: str) -> bool:
            strDict = {}
            for c in string:
                if c in strDict:
                    strDict[c] += 1
                else:
                    strDict[c] = 1
                    
            return strDict == charDict
        
        # Create hashmap of characters and their frequency of s1
        charDict = {}
        for ch in s1:
            if ch in charDict:
                charDict[ch] += 1
            else:
                charDict[ch] = 1
        
        len1 = len(s1)
        len2 = len(s2)
        for i in range(len2 - len1 + 1):
            if isPermutation(s2[i:i+len1]):
                return True
        
        return False
            
        
        