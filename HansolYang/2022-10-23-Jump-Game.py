class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        
        maximum = nums[0]
        
        for i in range(len(nums)):
            if maximum <= i and nums[i] == 0:
                return False
            
            if i + nums[i] > maximum:
                maximum = i + nums[i]
                
            if maximum >= len(nums) - 1:
                return True
                
        return False