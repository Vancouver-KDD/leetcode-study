# https://leetcode.com/problems/group-anagrams/description/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # { ate: [zxcv, zxcv, zxcv], qwe: [qwer] }
        # and return values
        hm = {}
        for item in strs:
            sortStr = "".join(sorted(item))
            hm[sortStr] = hm.get(sortStr, []) + [item]

        return hm.values()
