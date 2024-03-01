import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                # ord() gets unicode of characters
                count[ord(c) - ord("a")] += 1
            # using tuple as dictionary key should be immutable
            ans[tuple(count)].append(s)
        return ans.values()
s = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
s.groupAnagrams(strs)

'''explained'''
'''
SUMMARY: Using ord() and unicode characters
1. ord() function
The ord() function gives the Unicode code point of a character.
For English alphabets:

ord('a') returns 97
ord('b') returns 98
...
ord('z') returns 122

2. counter key examples using unicode function

- "eat" and its count key value
(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
 a           e                                            t

- "tan" and its count key value
(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
 a                                      n                 t



'''
