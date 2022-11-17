
# 424. Longest Repeating Character Replacement

> Problem link: https://leetcode.com/problems/longest-palindromic-substring/  
> submission detail: https://leetcode.com/submissions/detail/759773546/  

```py
class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ''
        res_len = 0

        for i in range(len(s)):

            # odd case
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l : r + 1]
                    res_len = r - l + 1
                l -= 1
                r += 1

            # even case
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l : r + 1]
                    res_len = r - l + 1
                l -= 1
                r += 1

        return (res)
```