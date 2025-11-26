class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []

        self.backtrack(candidates, target, 0, ans, curr)
        return ans

    def backtrack(self, candidates, target, start, ans, curr):
        if target == 0:
            ans.append(curr.copy())

        if target < 0:
            return

        for i in range(start, len(candidates)):
            curr.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i, ans, curr)
            curr.pop()
