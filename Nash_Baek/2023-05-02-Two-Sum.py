# For more description, please visit the blog below.
# https://peterdrinker.tistory.com/475
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Error handling part
        # Check the boundary of length, element and target
        if not (2 <= len(nums) <= 10**4 and -10**9 <= target <= 10**9):
            raise ValueError("Invalid boundary")
        for element in nums:
            if not -10**9 <= element <= 10**9:
                raise ValueError("Invalid boundary")

        # Calculate result = target - element(first to last index)
        # Find the result from second element to last element in the nested loop.
        # It requires O(N).
        # If the result does not find from the list, it continues the iteration.
        for element in nums:
            first_index = nums.index(element)
            result = target - element
            try:
                last_index = nums.index(result, (first_index + 1))
                return first_index, last_index
            except ValueError:
                continue
