class Solution:
    def combinationHelper(self, can, tar, canIndex, res, curr):
        if tar == 0:
            res.append(list(curr))
            return
        
        for i in range(canIndex, len(can)):
            if (tar - can[i]) >= 0:
                curr.append(can[i])
                self.combinationHelper(can, tar - can[i], i, res, curr)
                curr.remove(can[i])
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        r = []
        c = []
        self.combinationHelper(candidates, target, 0, r, c)
        return r