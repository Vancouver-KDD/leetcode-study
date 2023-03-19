class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for w in wordDict:
                if dp[i - len(w)] and s[:i].endswith(w):
                    dp[i] = True

        return dp[-1]