# [2,7,9,3,1]
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        dp[2] = max(nums[0]+nums[2], nums[1])
        for i in range(3, len(nums)): # 2 ~ 4 inclusive
            include_i = dp[i-2] + nums[i]
            exclude_i = dp[i-1]
            dp[i] = max(include_i, exclude_i)
        return dp[len(nums)-1]

nums = [6, 3, 10,  8,  2, 10, 3,  5,  10, 5, 3]
s = Solution()
s.rob(nums)

