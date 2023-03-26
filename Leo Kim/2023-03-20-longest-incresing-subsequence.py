class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        LIS = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)