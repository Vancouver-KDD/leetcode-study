class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        missing = n
        for i in range(n):
            missing ^= i
            missing ^= nums[i]
        return missing