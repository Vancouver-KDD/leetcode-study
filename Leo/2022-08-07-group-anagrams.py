class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for s in strs:
            groups[tuple(sorted(s))].append(s)
        return map(sorted, groups.values())