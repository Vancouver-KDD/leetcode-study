class Solution:
    def longestPalindrome(self, s: str) -> str:
        lsf = ""
        
        for i in range(len(s)):
            start = 1
            
            while (i - start >= 0 and i + start < len(s) and s[i-start] == s[i+start]):
                start += 1
                
            start -= 1
            
            curr = s[i-start:i+start+1]
            
            even = 0
            while (i-even >= 0 and i+even+1 < len(s) and s[i-even] == s[i+even+1]):
                even += 1
            
            even -= 1
                
            if ((i+even+1) - (i-even) + 1) > len(curr):
                curr = s[i-even:i+even+2]
            
            if len(curr) > len(lsf):
                lsf = curr
        
        return lsf