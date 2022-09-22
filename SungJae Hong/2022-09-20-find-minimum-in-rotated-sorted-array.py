from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = nums[0]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                min = nums[i+1]
                break
        return min

#Binary search method o (log n)
class Solution2:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res