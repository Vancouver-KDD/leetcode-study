# tabulation
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) < 1:
            return 0
        return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))

# memoization
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n
        def dp(i):
            if i >= n:
                return 0
            if memo[i] > -1:
                return memo[i]

            memo[i] = max(nums[i] + dp(i + 2), dp(i + 1))
            return memo[i]
        return dp(0)
