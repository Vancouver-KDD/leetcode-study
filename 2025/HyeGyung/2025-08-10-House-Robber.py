class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        prev2 = nums[0]  # dp[i-2]
        prev1 = max(nums[0], nums[1])  # dp[i-1]

        for i in range(2, n):
            cur = max(prev1, prev2 + nums[i])  # dp[i]
            prev2, prev1 = prev1, cur

        return prev1
