# 1. Check all substring  with map

# 2.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        n = len(s)

        if len(s) == 0: 
            return 0

        for left in range(0,n):
            for right in range(left, n):
                m = {}
                trigger = 0                
                sb = s[left:right+1]

                for ch in sb: 
                    if ch in m: 
                        trigger = 1
                        break
                    m[ch] = 1
                
                if trigger == 1: 
                    break

                maxLen = max(maxLen, len(sb))

        return maxLen
                
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         maxLen = 0
#         n = len(s)

#         for left in range(n):
#             m = {}
#             for right in range(left, n):
#                 ch = s[right]
#                 if ch in m:
#                     break
#                 m[ch] = 1
#                 maxLen = max(maxLen, right - left + 1)

#         return maxLen




