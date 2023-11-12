class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        def dfs(i):

            res = 0

            if i >= len(s):
                return 0

            for j in range(i + 1, len(s) + 1):
                tmp = s[i:j]
                if tmp not in visited:
                    visited.add(tmp)
                    res = max(res, 1 + dfs(j))
                    visited.remove(tmp)

            return res

        visited = set()
        return dfs(0)