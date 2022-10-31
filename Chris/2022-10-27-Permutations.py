class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        length = len(nums)
        numSet = set(nums)
        
        def dfs(cur, numSet,size):
            if size == length:
                res.append(cur)
                return
            
            for num in numSet:
                copySet = numSet.copy()
                copySet.remove(num)
                copyList = cur.copy()
                copyList.append(num)
                dfs(copyList, copySet, size+1)
        
        
        
        
        dfs([],numSet,0)
        
        return res
        
        