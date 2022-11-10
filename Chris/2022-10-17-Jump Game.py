class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        j = 0 # farthest reacheable index 
        
        for i in range(len(nums)-1):
            j = max(i + nums[i], j)
            
            if j >= len(nums)-1:
                return True
            
            if j <= i:
                return False
            
            
        
        return True
            
            
        