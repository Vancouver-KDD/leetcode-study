class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1

        while left_index <= right_index:
            mid_index = left_index + (right_index - left_index) // 2
            if nums[mid_index] == target:
                return mid_index
            elif nums[left_index] <= nums[mid_index]:
                if target >= nums[left_index] and target < nums[mid_index]:
                    right_index = mid_index
                else:
                    left_index = mid_index + 1
            else:
                if target > nums[mid_index] and target <= nums[right_index]:
                    left_index = mid_index + 1
                else:
                    right_index = mid_index
        return -1
