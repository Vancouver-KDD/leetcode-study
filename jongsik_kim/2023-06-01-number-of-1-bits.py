class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_count = 0
        for i in str(bin(n)):
            if i == "1":
                bit_count += 1
        return bit_count


s = Solution()
print(s.hammingWeight(int(input('Enter the #: '))))
