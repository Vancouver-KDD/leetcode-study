from typing import List 

class Solution:
    def wordBreak(s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[0] = True
        res = ""
        counter = 0
        while counter < len(s):
            for w in wordDict:
                if counter+len(w) <= len(s) and s[counter:counter+len(w)] == w:
                    res += w
                    counter += len(w) -1
                    break
            counter += 1
        return res == s
        
if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet","code"]
    Solution.wordBreak(s, wordDict)