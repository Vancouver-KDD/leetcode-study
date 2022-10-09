class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s)+1)
        dp[-1] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                word_len = len(word)
                if i + word_len <= len(s) and s[i:i + word_len] == word and dp[i + word_len]:
                    dp[i] = True

        return dp[0]