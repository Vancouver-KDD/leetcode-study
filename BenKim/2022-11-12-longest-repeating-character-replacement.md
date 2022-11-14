# 424. Longest Repeating Character Replacement

> Problem link: https://leetcode.com/problems/longest-repeating-character-replacement/  
> submission detail: https://leetcode.com/problems/longest-repeating-character-replacement/submissions/842994490/  

```py
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        res = 0

        l = 0
        for r in range(len(s)):
            # right 포인터를 이동하며 하나씩 붙임 
            counts[s[r]] = 1 + counts.get(s[r], 0)
            
            # replace가 필요한 문자가 k보다 많으면 left포인터를 하나씩 이동
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
```