class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        while n != 1:
            num = sum([int(x) ** 2 for x in str(n)])
            print(num)
            if num in hashset:
                return False
            hashset.add(num)
            n = num
        return True

        # TRY_1: cannot escape the loop when iterating
        # def make_happy(num):
        #     while num != 1:
        #         num = sum([int(x) ** 2 for x in str(num)])
        #         # how to escape?
        #     return True
        #
        # return make_happy(n)


s = Solution()
print(s.isHappy(int(input('Enter the #: '))))

# Input: n = 19
# Output: true

# Input: n = 2
# Output: false

# Input: n = 1111111
# Output: true
