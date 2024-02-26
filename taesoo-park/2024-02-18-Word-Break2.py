from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]):
        if not s:
            return True
        wordSet = set(wordDict)
        for i in range(len(s)):
            if s[:i] in wordSet:
                if self.wordBreak(s[i+1:], wordDict):
                    return True
            elif s[:i]
            

        

