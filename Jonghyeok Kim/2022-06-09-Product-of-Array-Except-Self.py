from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        res = [0] * nums_len
        prefix, postfix = 1, 1
        for idx, num in enumerate(nums):
            res[idx] = prefix
            prefix *= num
        for idx, num in enumerate(nums[::-1]):
            res[nums_len-1-idx] *= postfix
            postfix *= num
        return res