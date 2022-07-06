class Solution:
    def climbStairs(self, n: int) -> int:
        step_n, step_n1, step_n2 = 2, 1, 1
        for i in range(1, n+1):
            if i == 1:
                step_n1 = 1
            else:
                step_n = step_n1 + step_n2
                tmp = step_n1
                step_n1 = step_n
                step_n2 = tmp
        return step_n

# Cleaner Sol.
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for _ in range(n-1):
            tmp = one
            one = one + two
            two = tmp
        return one