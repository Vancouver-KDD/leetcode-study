class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(start, comb, comb_sum):

            if comb_sum == target:
                res.append(comb.copy())
                return
            if comb_sum > target:
                return
            dfs(start, comb + [candidates[start]], comb_sum + candidates[start])
            if start+1 <len(candidates):
                dfs(start + 1, comb, comb_sum)


        dfs(0, [], 0)
        return res