class Solution:
    def reverseBits(self, n: int) -> int:
        res, counter = 0, 0
        while n:
            res |= (n & 1) << (31-counter)
            counter += 1
            n = n >> 1
        return res