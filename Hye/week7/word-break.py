"""139. Word Break / Medium

Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated 
sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused 
multiple times in the segmentation.


Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
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
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        1. check if the string starts with one of the wordDict
        2. check for the rest of the string and update memo
        """
        memo = {}

        def helper(current_str, wordDict, memo):
            if current_str in memo:
                return memo[current_str]

            if not current_str:
                return True

            for word in wordDict:
                if current_str.startswith(word):
                    size = len(word)
                    new_str = current_str[size:]
                    if helper(new_str, wordDict, memo):
                        memo[current_str] = True
                        return True

            memo[current_str] = False
            return False

        return helper(s, wordDict, memo)
