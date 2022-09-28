class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans += n % 2
            n >>= 1
        return ans
