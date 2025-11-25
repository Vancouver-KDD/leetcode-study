class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        final_min = float('inf')

        while left <= right:
            mid = (left + right) // 2
            final_min = min(final_min, nums[mid])

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return final_min