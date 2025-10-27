class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_so_far = 0 
        seen = set()
        start, end = 0, 0
        while end < len(s):     
            while s[end] in seen: 
                seen.remove(s[start])
                start+=1 
            seen.add(s[end])
            max_so_far = max(max_so_far, end-start+1)
            end+=1 
        return max_so_far

