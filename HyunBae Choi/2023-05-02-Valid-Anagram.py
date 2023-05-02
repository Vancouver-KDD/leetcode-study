# Given two strings s and t, return true if t is an anagram of s, and false otherwise
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Constraints:
#   1 <= s.length, t.length <= 5 * 104
#   s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # two methods: sort the strings and iterate through each letter and compare based on index
        # or create a dictionary to store the number of occurrences for each letter and compare
        # edge case: if the length of "s" and "t" are different, can't be an anagram

        # implementation using sorted()
        # s_sorted = sorted(s)
        # t_sorted = sorted(t)
        # return s_sorted == t_sorted

        # implementation using dictionaries
        if len(s) != len(t):
            return False

        dict_s = {}
        dict_t = {}

        for i in range(len(s)):
            dict_s[s[i]] = dict_s.get(s[i], 0) + 1
            dict_t[t[i]] = dict_t.get(t[i], 0) + 1

        for char in dict_s:
            if dict_s[char] != dict_t.get(char, 0):
                return False

        return True
