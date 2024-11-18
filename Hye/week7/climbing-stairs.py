""" Climbing Stairs / Easy
 
You are given an integer n representing the number of steps to reach the top of a staircase.
You can climb with either 1 or 2 steps at a time.
Return the number of distinct ways to climb to the top of the staircase.

Example 1:
Input: n = 2
Output: 2
Explanation:
1 + 1 = 2
2 = 2

Example 2:
Input: n = 3
Output: 3
Explanation:
1 + 1 + 1 = 3
1 + 2 = 3
2 + 1 = 3

Constraints:
1 <= n <= 30
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        n = 1 -> 1 way (1)
        n = 2 -> 2 ways (1, 1),(2)
        n = 3 -> 3 ways (1, 1, 1)(1, 2)(2, 1)
        n = (n-1) + n-2
        """
        # Space Optimized
        if n <= 2:
            return n
        n1, n2 = 1, 2
        for i in range(3, n + 1):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        return n3

        # Other way
        # dp [0] * (n + 1)
        # dp[1], dp[2] = 1, 2
        # for i in range(3, n + 1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]

