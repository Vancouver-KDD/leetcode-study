class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)-1
        
        while l < r:
            mid = (l + r) // 2
            
            if nums[l] < nums[r]:
                return nums[l]
            
            if r - l == 1:
                return nums[r]
            
            if nums[l] < nums[mid]:
                l = mid
            else:
                r = mid
        
        return nums[l]