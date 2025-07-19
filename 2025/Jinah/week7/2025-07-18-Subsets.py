from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def create_subsets(i):
            if i == len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            create_subsets(i+1)

            subset.pop()
            create_subsets(i+1)

        create_subsets(0)

        return res