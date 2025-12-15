class Solution:
    def climbStairs(self, n: int) -> int:
        #
        # memo[i] + memo[i+1]
        # step[1] = 1
        # step[2] = 2
        # step[3] = 3

        step = [0] * (n + 1)
        #

        if n <= 1:
            return 1

        step[1] = 1
        step[2] = 2

        i = 1

        while i + 2 <= n:

            step[i + 2] = step[i] + step[i + 1]

            i += 1

        return step[n]
