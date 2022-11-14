class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # You will always replace characters that are not most frequent
        # Sliding window
        
        charCount = {}
        l = 0  # starting index of current consideration
        res = 0
        for r in range(len(s)):
            # update the incoming character
            charCount[s[r]] = charCount.get(s[r],0) + 1
            
            
            while r-l+1 - max(charCount.values()) > k:
                charCount[s[l]] -= 1
                l += 1
            res = max(r-l+1, res)
        
        return res
            
        
                
                
        