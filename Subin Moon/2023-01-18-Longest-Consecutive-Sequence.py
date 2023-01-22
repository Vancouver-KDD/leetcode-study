# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

class Solution:
    def longestConsecutive_O_logn(self, nums: list[int]) -> int:
        # Empty array
        if not nums:
            return 0

        # sort array
        nums.sort()
        current_count = 1
        longest_count = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] - nums[i-1] == 1:
                    current_count += 1
                else:
                    longest_count = max(longest_count, current_count)
                    current_count = 1

        return max(longest_count, current_count)

    def longestConsecutive_O_n(self, nums: list[int]) -> int:
        if not nums:
            return 0

        longest_count = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_count = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_count += 1

                longest_count = max(longest_count, current_count)

        return longest_count