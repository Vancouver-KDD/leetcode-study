class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        # total number of bits to represent integer
        bit_len = 32
        while bit_len > 0:
            ans <<= 1 # ans * 2
            ans += (n & 1)
            n >>= 1 # n // 2
            bit_len -= 1
        return ans