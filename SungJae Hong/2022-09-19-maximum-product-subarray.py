from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        #track the current maximum.
        curMin = 1
        #track the current minimum
        curMax = 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            temp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            result = max(result, curMax)
        return result