class Solution(object):
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid_index = (left + right) // 2

            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] < target:
                left = mid_index + 1
            else:
                right = mid_index - 1

        return -1
