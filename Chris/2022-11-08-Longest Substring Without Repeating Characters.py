class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Sliding window using two pointers
        substring = set()
        res = 0
        begin = 0
        for i in range(len(s)):
            
            while s[i] in substring:
                substring.remove(s[begin])
                begin += 1
            substring.add(s[i])
            res = max(res,i-begin+1)
        return res
                
            
            
            
        
            
        
        
        
    