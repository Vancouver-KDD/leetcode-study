# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums.
# If target exists, then return its index.
# Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        last_index = len(nums) -1
        start_index = 0

        while start_index <= last_index:
            mid_index = (last_index + start_index) //2

            if nums[mid_index] == target:
                return mid_index
            if nums[mid_index] < target:
                start_index = mid_index + 1
            else :
                last_index = mid_index -1


        return -1