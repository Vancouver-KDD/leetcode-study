class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        prefix, postfix = 1, 1
        res = [1] * nums_len
        for idx in range(1,nums_len):
            prefix *= nums[idx-1]
            res[idx] = prefix
        for idx in range(nums_len-2,-1,-1):
            postfix *= nums[idx+1]
            res[idx] *= postfix
        return res