class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def back_tracking(path, remain, first_index):
            if remain == 0:
                res.append(path[:])
                return
            if remain < 0:
                return
            for i in range(first_index, len(candidates)):
                if i > first_index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                back_tracking(path, remain-candidates[i], i+1)
                path.pop()

        back_tracking([], target, 0)
        return res