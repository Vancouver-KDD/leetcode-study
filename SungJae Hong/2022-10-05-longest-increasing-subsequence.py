from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Cache of list.
        LIS = [1] * len(nums)

        # Go through the list backwards
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                # only update list when nums[j] is bigger value.
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)