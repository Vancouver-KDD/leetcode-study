# 139. Word Break

> Problem link: https://leetcode.com/problems/word-break/  
> submission detail: https://leetcode.com/submissions/detail/819005422/

```py
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:

                    # 뒤의 단어들이 참인경우에만 현재도 참이 될 수 있다 
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
```