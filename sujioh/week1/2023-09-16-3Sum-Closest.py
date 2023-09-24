# Input: nums = [-1,2,1,-4], target = 1
# Output: 2

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):  # i = start index of sub array
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if abs(target - curr_sum) < abs(target - closest_sum):
                    closest_sum = curr_sum

                if target < curr_sum:
                    right = right - 1
                else:
                    left = left + 1

        return closest_sum

# This function first sorts the input list 'nums' in ascending order.
# It then employs a two-pointer approach, utilizing 'i' as the starting index of subarrays.
# For each subarray, it calculates the sum and updates 'closest_sum'
# if a closer sum to the target is found.
# The 'left' and 'right' pointers are adjusted based on the comparison between 'curr_sum' and 'target.'
# This process efficiently identifies the closest sum.

# Example:
# For input [4, -1, 1, 2], it categorizes subarrays based on 'i':

# Category 1 (i = 0): [4, -1, 1] and [4, 1, 2]
# Category 2 (i = 1): [-1, 1, 2]
# The function successfully finds the closest sum using sorting and the two-pointer technique.
# Time complexity: O(n^2), space complexity: O(1).
