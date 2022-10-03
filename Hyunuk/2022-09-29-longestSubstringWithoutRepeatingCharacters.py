import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = collections.defaultdict(int)
        l = 0
        r = 0
        ret = 0
        while r < len(s):
            window[s[r]] += 1
            while window[s[r]] > 1:
                window[s[l]] -= 1
                l += 1
            ret = max(ret, r - l + 1)
            r += 1
        
        return ret
