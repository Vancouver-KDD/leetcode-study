# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         count = {}
#         res = 0
#         l = 0
#         for r in range(len(s)):
#             count[s[r]] = 1 + count.get(s[r], 0)
#             while (r-l+1) - max(count.values()) > k:
#                 count[s[l]] -= 1
#                 l += 1
#             res = max(res, r - l + 1)
#         return res

class Solution:
    def characterReplacement(s: str, k: int) -> int:
        hash_map = {}
        left, right, res = 0, 0, 0
        for idx, elem in enumerate(s):
            hash_map[elem] = hash_map.get(elem, 0) + 1
            max_count = max(hash_map.values())
            while right-left+1 - max_count > k:
                hash_map[s[left]] -= 1 
                left += 1
            res = max(res, right-left+1)
            right += 1
        return res

if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    Solution.characterReplacement(s,k)