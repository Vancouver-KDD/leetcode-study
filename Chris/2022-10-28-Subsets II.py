class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        # Sort array
        nums.sort()
        
        def dfs(cur, i):
            print(cur, i)
            
            if i >= len(nums):
                res.append(cur)
                return
            
            copyList1 = cur.copy()
            copyList2 = cur.copy()
            copyList1.append(nums[i])
            dfs(copyList1, i+1)
            
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i +=1
            dfs(copyList2,i+1)
            
        dfs([],0)
        
        return res
            
        
        