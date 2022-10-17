class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        # curList: Partial List of answer
        def dfs(curList, curSum, index):
            if curSum > target or index >= len(candidates):
                return
            
            if curSum == target:
                res.append(curList.copy())
                return
            
            
            curList.append(candidates[index])
            dfs(curList, curSum+candidates[index], index)
            curList.pop()
            dfs(curList, curSum, index+1)
            return
        
        
        dfs([], 0, 0)
        
        return res                    