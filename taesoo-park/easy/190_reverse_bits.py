class Solution:
    def reverseBits(num):
        result = 0
        for i in range(32):
            result = (result << 1) | ((num >> i) & 1)
        return result