class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            return s[l:r+1]
        if len(s) == 1:
            return s
        elif len(s) == 2:
            return s if s == s[::-1] else s[0]
        ret = ""
        for i in range(1, len(s)):
            odd = helper(i, i)
            even = helper(i-1, i)
            ret = max(ret, odd, even, key=len)
        return ret
