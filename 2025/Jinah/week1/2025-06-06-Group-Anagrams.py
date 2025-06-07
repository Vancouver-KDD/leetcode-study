from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            dict[key].append(word)
        
        return list(dict.values())