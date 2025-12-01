class Solution(object):
    def combinationSum(self, candidates, target):
        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                results.append(list(comb))
                return
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i)
                comb.pop()

        backtrack(target, [], 0)
        return results
