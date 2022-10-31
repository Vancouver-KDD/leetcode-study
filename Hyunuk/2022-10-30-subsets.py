class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(arr, start):
            if len(arr) == k:
                ret.append(arr[:])
            for i in range(start, len(nums)):
                arr.append(nums[i])
                helper(arr, i+1)
                arr.pop()
        ret = []
        for k in range(len(nums)+1):
            helper([], 0)
        return ret
