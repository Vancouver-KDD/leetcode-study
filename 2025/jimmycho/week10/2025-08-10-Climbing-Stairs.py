from math import factorial

class Solution:
    def climbStairs(self, n: int) -> int:
        res = 1
        for i in range(1, n // 2 + 1):
            res += factorial((n - 2 * i) + i) / factorial(i) / factorial(n - 2 * i)
        return int(res)