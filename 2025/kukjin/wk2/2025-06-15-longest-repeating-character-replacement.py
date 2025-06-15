# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         maxLen = 0 
#         n = len(s)


#         for left in range(n):
#             m = {}
#             max_key = s[left]
#             max_count = 1
#             for right in range(left, n):
#                 # if s[right] not in m:
#                 #     m[s[right]] = 1
#                 # else:
#                 #     m[s[right]] = m.get(s[right]) + 1
#                 m[s[right]] = m.get(s[right], 0) + 1

#                 if max_count < m[s[right]]:
#                     max_count = m[s[right]]
#                     max_key = s[right]

#                 # max_key = max(m, key=m.get)
#                 # sum_value = 0 
#                 # for key, value in m.items(): 
#                 #     if key == max_key:
#                 #         continue 
#                 #     sum_value += value
#                 sum_value = sum(m.values()) - max_count
 

#                 if sum_value <= k:
#                     maxLen = max(maxLen, right - left + 1)

#         return maxLen 

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0 
        m = {}
        max_count = 0
        left = 0

        for right in range(len(s)):
            m[s[right]] = m.get(s[right], 0) + 1
            max_count = max(max_count, m[s[right]])

            # If more than k replacements needed, shrink window
            while (right - left + 1) - max_count > k:
                m[s[left]] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen



