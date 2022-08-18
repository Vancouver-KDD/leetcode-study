class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        
        for i in range(len(s)):
            
            index = 0
            
            while (i-index>=0 and i+index<len(s) and s[i-index]==s[i+index]):
                res += 1
                index += 1
                
            index = 0
            
            while (i-index>=0 and i+index+1<len(s) and s[i-index]==s[i+index+1]):
                res += 1
                index += 1
            
        return res