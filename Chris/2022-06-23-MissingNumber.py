class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        return (int)(size * (size + 1) / 2) - sum(nums)
        