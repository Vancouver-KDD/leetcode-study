class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for n in nums[1:]:
            res ^= n
        return res
        