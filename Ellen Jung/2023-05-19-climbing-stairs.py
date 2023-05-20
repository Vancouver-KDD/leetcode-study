class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 3:
            return n

        ways = 0
        x = 1
        y = 2

        for z in range(4, n + 1):
            ways = x + y
            x = y
            y = ways

        return ways