class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:

        def dfs(start, arr):
            if start > n + 1:
                return

            if len(arr) == k:
                result.append(arr[:])
                return

            for i in range(start, n + 1):
                arr.append(i)
                dfs(i + 1, arr)
                arr.pop()

        result = []
        dfs(1, [])
        return result