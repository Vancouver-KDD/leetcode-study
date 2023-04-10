class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0

        while n:
            num += 1
            n = n & (n - 1)

        return num