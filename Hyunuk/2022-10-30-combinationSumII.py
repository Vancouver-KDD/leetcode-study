class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def bt(remainder, arr=[], start=0):
            if remainder < 0:
                return
            if remainder == 0:
                ret.append(arr[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if remainder - candidates[i] < 0:
                    break
                arr.append(candidates[i])
                bt(remainder-candidates[i], arr, i+1)
                arr.pop()
            
        candidates.sort()
        ret = []
        bt(target, [], 0)
        return ret
