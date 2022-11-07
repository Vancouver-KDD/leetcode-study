class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        candidates.sort()
        
        
        
        
        def dfs(combo, total, i):
            if total == target:
                res.append(combo.copy())
                return
                
            if i >= len(candidates) or total > target:
                return
            
            
            
            newCombo = combo.copy()
            # case where current value is added
            newCombo.append(candidates[i])
            dfs(newCombo, total+candidates[i], i+1)
            newCombo.pop()
            # case where current value is not added
            # prevent duplicate by completely exclding the current value  
            while i < len(candidates)-1 and  candidates[i] == candidates[i+1]:
                i += 1
                
            
            dfs(newCombo, total, i+1)

            
        dfs([],0,0)
        
        return res
                
            
                