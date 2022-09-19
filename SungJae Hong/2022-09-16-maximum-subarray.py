from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Start by putting the very first value as the maximum number.
        maxi = nums[0]
        #Counter to track the current maximum value.
        counter = 0
        for n in nums:
            # If prefixes are negative number reset the counter to 0
            if counter < 0: counter = 0
            counter += n
            maxi = max(maxi, counter)
        return maxi
