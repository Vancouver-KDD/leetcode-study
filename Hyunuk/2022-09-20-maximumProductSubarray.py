class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret = float("-inf")
        max_ = min_ = nums[0]
        ret = max_
        for i in range(1, len(nums)):
            curr = nums[i]
            max_, min_ = max(curr, max_ * curr, min_ * curr), min(curr, max_ * curr, min_ * curr)
            ret = max(max_, ret)
        return ret

