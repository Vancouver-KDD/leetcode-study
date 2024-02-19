class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True

        for word in wordDict:
            if s.startswith(word):    
                if self.wordBreak(s[len(word):], wordDict):
                    return True
        
        return False

s = "leetcode"
wordDict = ["leet","code"]
sol = Solution()
print(sol.wordBreak(s, wordDict))