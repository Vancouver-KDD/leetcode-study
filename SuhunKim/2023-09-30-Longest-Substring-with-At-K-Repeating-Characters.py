class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # ### method 1 (brute force) => O(n^2), O(1) : TLE
        # res = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         cnt = collections.Counter(s[i:j+1])
        #         # print(i, j, cnt)
        #         temp = 0
        #         flag = True
        #         for char in cnt:
        #             if cnt[char] >= k:
        #                 temp += cnt[char]
        #             else:
        #                 flag = False
        #         if flag:
        #             res = max(res, temp)
        # return res
        
        # ### method 2 (from the possible maximum numbers from 1) : O(n^2), O(1) : TLE
#         for i in range(len(s),k-2,-1):
#             for j in range(len(s)-i):
#                 cnt = collections.Counter(s[j:i+j+1])
#                 print(i, j, cnt)
#                 temp = 0
#                 flag = True
#                 for char in cnt:
#                     if cnt[char] >= k:
#                         temp += cnt[char]
#                     else:
#                         flag = False
#                 if flag:
#                     return temp
#         return 0 
        
        ### method 3
        charCnts = collections.Counter(s)
        flag = True
        for char in charCnts:
            if charCnts[char] < k:
                s = s.replace(char, ";")
                flag = False
        if flag:
            return len(s)
        else:
            return max(self.longestSubstring(new_s, k) for new_s in s.split(";"))