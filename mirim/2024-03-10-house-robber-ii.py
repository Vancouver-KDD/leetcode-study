# https://leetcode.com/problems/house-robber-ii/description/


class Solution:
    def rob(self, nums: List[int]) -> int:
        def func(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            return dp[-1]

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2 or len(nums) == 3:
            return max(nums)

        return max(func(nums[:-1]), func(nums[1:]))
