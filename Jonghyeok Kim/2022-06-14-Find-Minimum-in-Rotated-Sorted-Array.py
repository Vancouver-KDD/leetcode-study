from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        res = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                return min(nums[left], res)
            middle = left + ((right-left) // 2)
            
            res = min(nums[middle],res)
            
            if nums[left] <= nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return res