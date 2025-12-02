class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # [2,3,6,7]
        # [3 3]

        res = []
        subset = []

        def backtracking(index, curr_sum):
            if curr_sum > target:
                return
            if curr_sum == target:
                res.append(subset[:])
                return
            for i in range(index, len(candidates)):
                subset.append(candidates[i])
                backtracking(i, curr_sum + candidates[i])
                subset.pop()

        backtracking(0, 0)
        return res