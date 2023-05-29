class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1") # 1

# 1. bin(n ^ 00000000000000000000000000000000).count('1')