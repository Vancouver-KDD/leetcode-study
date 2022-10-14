class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.partial_rob(nums[1:]), self.partial_rob(nums[:len(nums)-1]))
    
    def partial_rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        for i in range(2, len(nums)):
            nums[i] += max(nums[:i-1])
                
        return max(nums[-1], nums[-2])