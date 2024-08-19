class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] += 1
        for num in nums:
            temp_dp = defaultdict(int)
            for memory in dp:
                temp_dp[memory + num] += dp[memory]
                temp_dp[memory - num] += dp[memory]
            dp = temp_dp

        return dp[target]