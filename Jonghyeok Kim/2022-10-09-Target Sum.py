class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:  
        # key: (index, total)
        # value: # of ways
        dp = {}
        def dfs(i, cur_sum):
            if i == len(nums):
                return 1 if cur_sum == target else 0
            if (i, cur_sum) in dp:
                return dp[(i, cur_sum)]
            dp[(i, cur_sum)] = dfs(i+1, cur_sum+nums[i]) + dfs(i+1, cur_sum-nums[i])
            return dp[(i, cur_sum)]
        dfs(0,0)
        return dp[(0,0)]