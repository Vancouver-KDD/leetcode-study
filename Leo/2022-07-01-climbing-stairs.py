class Solution:
    def climbStairs(self, n: int) -> int:
        f1, f2 = 1, 0
        for f in range(n):
            f1, f2 = f1 + f2, f1

        return f1