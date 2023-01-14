class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))

            if sorted_s not in ans:
                ans[sorted_s] = []

            ans[sorted_s].append(s)

        return list(ans.values())

        ## Time complexity: O(m * nlogn)