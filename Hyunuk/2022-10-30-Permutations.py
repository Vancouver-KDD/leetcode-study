class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(start):
            if start == len(nums):
                ret.append(nums[::])
            else:
                for i in range(start, len(nums)):
                    nums[start], nums[i] = nums[i], nums[start]
                    helper(start+1)
                    nums[start], nums[i] = nums[i], nums[start]
        ret = []
        helper(0)
        return ret
