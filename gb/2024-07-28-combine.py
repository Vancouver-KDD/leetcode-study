class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        subList = []

        def backtrack(start, subList):
            if len(subList) == k:
                res.append(subList[:])
                return
            for i in range(start, n+1):
                subList.append(i)
                backtrack(i+1, subList)
                subList.pop()
        backtrack(1, subList)
        return res
