class Solution:
    # O(n^2)
    def lengthOfLongestSubstring(self, s: str) -> int:        
        def getSubstringLength(i):
            
            substring = set()
            
            length = 0
            for c in s[i:]:
                if c in substring:
                    return length
                
                substring.add(c)
                length += 1
            
            return length
        
        maxLen = 0
        for i in range(len(s)):
            curr = getSubstringLength(i)
            if curr > maxLen:
                maxLen = curr
        
        return maxLen
            
#O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Sliding window using two pointers
        substring = set()
        
        l = 0
        
        res = 0
        for r in range(len(s)):
            
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
                
            substring.add(s[r])
                
            res = max(res, r-l+1)
            
        
        return res
            
            
            
            
        
            
        
        
        
        
        
        