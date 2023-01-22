from typing import List
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = collections.defaultdict(list)
        for s in strs:
            sorted_string = sorted(s)
            ans[tuple(sorted_string)].append(s)
        return list(ans.values())
    
    
input = ["eat","tea","tan","ate","nat","bat"]

Solution.groupAnagrams(Solution, input)
