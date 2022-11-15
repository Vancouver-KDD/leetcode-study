class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(l, r):
            word = s[l:r+1]
            cnt = 0
            while l >= 0 and r < len(s) and word == word[::-1]:
                cnt += 1
                l -= 1
                r += 1
                word = s[l:r+1]
            return cnt
        ret = 0
        for i in range(1, len(s)):
            ret += helper(i, i) + helper(i-1, i)
        return ret + 1
