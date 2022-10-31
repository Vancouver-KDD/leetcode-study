class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = collections.defaultdict(list)
        for s in strs:
            arr = list(s)
            arr.sort()
            hm[''.join(arr)].append(s)
        return hm.values()
        