# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target = some_number_from_nums + current_number, except itself
        # therefore, we can use dictionary to store the occurrences of each number in "nums"
        # and check of target - current_number exists, else add it to the dictionary
        # when storing the number in the dictionary, we want to store the number as the key and the index as the value

        nums_dict = {}
        for index, number in enumerate(nums):
            if target - number in nums_dict:
                return [index, nums_dict[target - number]]
            nums_dict[number] = index
