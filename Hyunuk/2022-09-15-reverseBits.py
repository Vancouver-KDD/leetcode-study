class Solution:
    def reverseBits(self, n: int) -> int:
        num = bin(n)[2:]
        num = ''.join(["0"] * (32 - len(num))) + num
        return int(num[::-1], 2)
