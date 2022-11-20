from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        #Start at $0
        rob1 = 0
        rob2 = 0

        for n in nums:
            # Store it in temp so that rob1 value doesn't switch for rob2.
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2