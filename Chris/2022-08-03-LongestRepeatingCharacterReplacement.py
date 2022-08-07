class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charCount = {}
        l = 0
        res = 0
        for r in range(len(s)):
            charCount[s[r]] = charCount.get(s[r],0) + 1
            
            while r-l+ 1 - max(charCount.values()) > k:
                charCount[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res
            
                
                
        