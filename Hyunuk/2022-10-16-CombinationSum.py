class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []

        def backtrack(remain, comb, start):
            if remain == 0:
                ret.append(comb[:])
                return
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i)
                comb.pop()

        backtrack(target, [], 0)

        return ret
