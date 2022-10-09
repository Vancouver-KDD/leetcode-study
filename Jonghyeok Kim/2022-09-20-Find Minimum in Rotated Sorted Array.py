class Solution:
    def findMin(self, nums: List[int]) -> int:
        #if all sorted, the first elem is the res
        #if left is sorted, check the right
        left, right = 0, len(nums) -1
        res = nums[0]
        while left <= right:
            middle = left + ((right-left) // 2)
            if nums[left] <= nums[right]:
                return min(res, nums[left])
            res = min(res, nums[middle])
            if nums[left] <= nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return res