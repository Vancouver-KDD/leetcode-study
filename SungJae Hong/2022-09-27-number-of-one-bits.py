class Solution:
    def hammingWeight(self, n: int) -> int:
        # Count the number of 1s.
        counter = 0
        while n != 0:
            # n % 2 will return 1 when n's rightmost value is 1.
            counter += n % 2
            # shift the left value to the right.
            n = n >> 1
        return counter
