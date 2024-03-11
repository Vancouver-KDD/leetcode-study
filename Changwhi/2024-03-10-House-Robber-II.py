class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums):
        first, secondAndMax = 0, 0
        for num in nums:
            tempMax = max(num + first, secondAndMax)
            first = secondAndMax
            secondAndMax = tempMax
        return secondAndMax
    
        
        
        
