class Solution:
    def search(self, nums: List[int], target: int) -> int:


        size = len(nums)
        left = 0
        right = size - 1

        while left <= right:
            # update middle preventing overflow
            mid = (right - left)// 2 + left

            if nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid -1

            else:
                return mid

        return -1
