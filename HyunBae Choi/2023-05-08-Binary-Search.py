# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Constraints:
# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

# 1. assign 2 pointers: "left" and "right"
# 2. while left <= right, find the "middle" index ("right" - "left") and check if the target is in that index
# 3. if "middle" is not the target, compare if target is less than or greater than the number at the "middle"
# 4. if "middle" is less than the target, discard the right side, else discard the left side
# 5. reset left or right, then repeat until target is found, or if target is not found, return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (right + left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1

        return -1
