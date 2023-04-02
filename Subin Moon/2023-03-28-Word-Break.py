"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""
class Solution:
    # O(n * m * n) -> word len n, wordDict len m
    # decision tree:
    # i = 0 (index of s) -> match each word in the wordDict
    # i -> 4 (the lens of the matched word in the wordDict) -> match each word in the wordDict again
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # Track if the subword is in the wordDict
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # Base case
        # Starting from the end and see if the index matches any word in the wordDict
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    # No enough chars to compare with w
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]


