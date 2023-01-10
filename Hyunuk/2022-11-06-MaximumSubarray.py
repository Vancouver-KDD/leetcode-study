class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]
        sub = nums[0]
        for i in range(1, len(nums)):
            sub = max(nums[i], sub+nums[i])
            ret = max(ret, sub)
        return ret
