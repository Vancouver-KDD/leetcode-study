# 647. Palindromic Substrings

> Problem link: https://leetcode.com/problems/palindromic-substrings/  
> submission detail: https://leetcode.com/problems/palindromic-substrings/submissions/845598685/  

```py
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # odd case
            l = r = i
            res += self.countPalin(s, l, r)

            # even case
            l, r = i, i + 1
            res += self.countPalin(s, l, r)
        return res

    def countPalin(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
```