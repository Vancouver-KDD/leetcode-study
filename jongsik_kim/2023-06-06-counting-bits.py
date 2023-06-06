class Solution:
    def countBits(self, n: int) -> list[int]:
        if n < 0 or n > 10**5:
            raise ValueError('Invalid Range')
        # TRY_1
        # Initialize the array
        d = [0] * (n + 1)
        for i in range(1, n + 1):
            # convert int to bin(str)
            bin_num = bin(i)[2:]
            occurs = bin_num.count('1')
            d[i] = occurs
        return d


s = Solution()
print(s.countBits(int(input('Enter the #: '))))

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

# TC: O(NlogN) -> O(N)
