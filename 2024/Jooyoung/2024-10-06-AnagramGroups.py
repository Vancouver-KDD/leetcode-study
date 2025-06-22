from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            c = [0] * 26

            for l in s:
                c[ord(l) - ord('a')] += 1

            ct = tuple(c)

            if ct in d:
                d[ct].append(s)
            else:
                d[ct] = [s]

        return list(d.values())


solution = Solution()
result = solution.groupAnagrams(["act","pots","tops","cat","stop","hat"])
print(result)
