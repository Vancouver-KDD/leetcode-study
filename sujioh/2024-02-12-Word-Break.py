# Given a string s and a dictionary of strings wordDict, 
# return true if s can be segmented into 
# a space-separated sequence of one or more dictionary words.'

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

from typing import List

# Given a string s and a dictionary of strings wordDict, 
# return true if s can be segmented into 
# a space-separated sequence of one or more dictionary words.'

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        # Each index i of dp represents 
        # whether the substring s[i:] 
        # can be segmented into words from the given wordDict.
        dp[len(s)] = True
        
        for i in range(len(s)-1, -1, -1): # 7~0 inclusive
            for w in wordDict:
                if dp[i]:
                    break
                in_range = i + len(w) <= len(s)
                if in_range and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
        # print(dp[0])
        return dp[0]
    
# s = "leetcode", 
# wordDict = ["leet","code"]

