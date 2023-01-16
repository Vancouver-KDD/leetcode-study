class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            key = str(sorted(s))
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = [s]

        return dic.values()
