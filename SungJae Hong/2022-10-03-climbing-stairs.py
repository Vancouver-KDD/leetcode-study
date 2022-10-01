class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        # Start from the back.
        # If n is 5 -> Stair 5, 4, 3, 2, 1, 0
        # Since we know stair 5 and stair 4 have 2 ways in total. We start from there.
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one