class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in str(bin(n)):
            if i == "1":
                count += 1
        return count


s = Solution()
print(s.hammingWeight(int(input('Enter the #: '))))
