class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(step):
            if(step <= 2):
                return step
            if step in memo:
                return memo[step]
            memo[step] = helper(step - 1) + helper(step - 2)
            return memo[step]
        return helper(n)