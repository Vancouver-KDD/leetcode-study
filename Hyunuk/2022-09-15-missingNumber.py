class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_ = max(nums)
        expected_sum = (max_ * (max_ + 1)) // 2
        return expected_sum - sum(nums)
