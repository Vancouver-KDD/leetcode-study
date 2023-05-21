class Solution:
    def climbStairs(self, n: int) -> int:
        last, secondLast = 1, 1
        for _ in range(n-1, 0, -1):
            temp = secondLast
            secondLast += last
            last = temp
        return secondLast