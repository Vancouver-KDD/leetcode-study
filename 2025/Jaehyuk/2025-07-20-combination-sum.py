class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(curr, total, i):
            if total == target:
                res.append(curr.copy())
                return 
            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(curr, total + candidates[i], i)
            curr.pop()
            dfs(curr, total, i + 1)
        dfs([], 0, 0)
        return res