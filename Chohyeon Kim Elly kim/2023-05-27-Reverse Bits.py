class Solution:
    def reverseBits(self, n: int) -> int:

        # get a bit from i'th position = 0 or 1
        # put it to 31- i'th position = bit << 31- i'th

        res = 0

        # 0 ^ 1 = 0
        # 1 ^ 1 = 1

        for i in range(32):
            bit = (n >> i) & 1

            res = res | (bit << (31 - i))

        return res

