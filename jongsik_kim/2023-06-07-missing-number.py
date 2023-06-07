class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        if len(nums) < 1 or len(nums) > 10**4:
            raise ValueError('Invalid Range')
        for i in range(len(nums) + 1):
            if i not in nums:
                return i


s = Solution()
l1 = [3, 0, 1]
l2 = [0, 1]
l3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(s.missingNumber(l1))
print(s.missingNumber(l2))
print(s.missingNumber(l3))
