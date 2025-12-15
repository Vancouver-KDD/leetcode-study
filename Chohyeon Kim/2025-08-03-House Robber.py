class Solution:
    def rob(self, nums: List[int]) -> int:
        # Top down + memo
        memo = {}
        # base case
        # when index <= 0 return

        # find max!

        def dfs(index: int) -> int:

            if index == 0:
                return nums[index]

            if index < 0:
                return 0

            if index in memo:
                return memo[index]

            res = 0

            res = max(res, nums[index] + dfs(index - 2), dfs(index - 1))

            memo[index] = res
            return res

        max_rob = dfs(len(nums) - 1)

        return max_rob
