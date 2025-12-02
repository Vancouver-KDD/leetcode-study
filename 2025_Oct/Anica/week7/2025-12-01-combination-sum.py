
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(i, path, summation):
            if summation == target and i <= len(candidates):
                res.append(path.copy())
                return 
            if i >= len(candidates) or summation > target: 
                return 

            else: 
                path.append(candidates[i])
                backtracking(i, path, summation+candidates[i])
                path.pop()
                backtracking(i+1, path, summation)

        backtracking(0, [], 0)
        return res






        