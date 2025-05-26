""" Anagram Groups
Given an array of strings strs, group all anagrams together into sublists.
You may return the output in any order.

An anagram is a string that contains the exact same characters as another string,
but the order of the characters can be different.

Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.

python hye/2024-10-03-group-anagrams.py
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagrams:
                anagrams.append(sorted_word)
        
        mapping = defaultdict(list)
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            mapping[sorted_word].append(word)
        
        for key, value in mapping.items():
            value.sort()
        return sorted(list(mapping.values()))
    

def main():
    s = Solution()

    # Example 1
    input = ["act","pots","tops","cat","stop","hat"]
    expected_output = sorted([["hat"],["act", "cat"],["stop", "pots", "tops"]])

    for anagram in expected_output:
        anagram.sort()
    ans = s.groupAnagrams(input)
    assert expected_output == ans

    # Example 2
    input =  ["x"]
    expected_output = [["x"]]

    for anagram in expected_output:
        anagram.sort()
    ans = s.groupAnagrams(input)
    assert expected_output == ans

    # Example 3:
    input = [""]
    expected_output = [[""]]
    
    for anagram in expected_output:
        anagram.sort()
    ans = s.groupAnagrams(input)
    assert expected_output == ans

    print("Success!")

    
if __name__ == "__main__":
    main()

    # Time Complexity: O(N) Linear
    # Space Complexity: O(N) Linear
