class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >>i) &1
            res |= (bit<<(31-i))
        return res

        # counter, res = 31, 0
        # while n:
        #     if n % 2 == 1:
        #         res += 2**counter
        #     n = n >> 1
        #     counter -= 1
        # return res
    