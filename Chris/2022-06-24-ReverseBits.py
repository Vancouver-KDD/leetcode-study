class Solution:
    def reverseBits(self, n: int) -> int:
        reversedBits = 0;
        for i in range(32):
            if n & 1 == 1:
                reversedBits += (2 ** (31-i))
            n = n >> 1
            
        return reversedBits
        