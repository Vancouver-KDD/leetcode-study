"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            return climb(n-1) + climb(n-2)
        return climb(n)

    def climbStairs_recursion(self, n):
        tmp = {}
        tmp[1] = 1
        tmp[2] = 2

        def climb(n):
            if n in tmp:
                return tmp[n]
            else:
                tmp[n] = climb(n-1) + climb(n-2)
                return tmp[n]

        return climb(n)