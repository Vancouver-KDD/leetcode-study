from collections import Counter


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        for string in strs:
            string_elements = frozenset(Counter(string).items())
            if string_elements in anagrams:
                anagrams[string_elements].append(string)
            else:
                anagrams[string_elements] = [string]
        return [anagram for counter, anagram in anagrams.items()]