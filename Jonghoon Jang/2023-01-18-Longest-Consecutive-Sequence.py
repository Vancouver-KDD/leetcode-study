"""
128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""


class Solution:
    # HashSet
    # Time complexity: O(N): HashSet(Set) O(1) lookup
    # Space complexity: O(n): for hashset
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        unique_nums = set(nums)  # O(n) space

        longest_num_sequence = 1
        curr_num_sequence = 1
        for num in unique_nums:
            # check if it is the first element of a sequence
            if num - 1 not in unique_nums:
                # only runs when the num is at beginning of a sequence
                while num + 1 in unique_nums:  # only run n iterations throughout the runtime
                    num += 1
                    curr_num_sequence += 1

                longest_num_sequence = max(curr_num_sequence, longest_num_sequence)
                curr_num_sequence = 1

        return longest_num_sequence

    # Sort
    # Time complexity: O(n * logn): for sorting
    # Space complexity: O(1): sort the input in place
    def longestConsecutiveSort(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        max_len = 1
        curr_len = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    curr_len += 1
                else:
                    max_len = max(max_len, curr_len)
                    curr_len = 1
        return max(max_len, curr_len)


def main():
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(s.longestConsecutiveSort([100, 4, 200, 1, 3, 2]))

    print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(s.longestConsecutiveSort([0,3,7,2,5,8,4,6,0,1]))

    print(s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
    print(s.longestConsecutiveSort([9,1,4,7,3,-1,0,5,8,-1,6]))


if __name__ == "__main__":
    main()
