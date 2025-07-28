class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index, _target, combination):
            if _target == 0:
                res.append(combination[:])
                return
            if index == len(candidates):
                return

            dfs(index + 1, _target, combination)
            curr = candidates[index]
            if curr <= _target:
                combination.append(curr)
                dfs(index, _target - curr, combination)
                combination.pop()

        dfs(0, target, [])
        return res
