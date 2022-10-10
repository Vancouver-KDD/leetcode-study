class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) +1) # track previous break point
        dp[0] = True # empty string always return True
        
        for idx in range(len(s)+1):
            for word in wordDict:
                # skip out of bound idx
                if idx - len(word) >= 0: 
                    if word == s[idx-len(word): idx] and dp[idx-len(word)]:
                        dp[idx] = True
        return dp[-1]