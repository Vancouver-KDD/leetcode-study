class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        l = 0
        r = len(nums) - 1
        
        while l < r:
            
            m = (l+r)//2
            
            if nums[m-1] > nums[m]:
                return nums[m]
            
            if nums[l] < nums[r]:
                return nums[l]
            
            if nums[r] < nums[r-1]:
                return nums[r]
            
            if nums[l] < nums[m]:
                l = m
            else:
                r = m