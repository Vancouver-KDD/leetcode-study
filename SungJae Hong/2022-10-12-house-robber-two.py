from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # get the maximum value of 3 values. Nums[0] is for edge case when there is only 1 house in the list.
        # get the max value without the first house and without last house.
        return max(nums[0],self.helper(nums[1:]), self.helper(nums[:-1]))

    # helper function. This is basically solution for house robber 1 question.
    def helper(self, nums):
        rob1 = 0
        rob2 = 0
        for n in nums:
            newRob = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

