class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                continue
            ret[i] = nums[i-1] * ret[i-1]
        acc = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                continue
            acc *= nums[i+1]
            ret[i] *= acc
        return ret
