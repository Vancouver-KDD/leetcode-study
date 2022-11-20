class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def bt(arr, start):
            if len(arr) == k:
                ret.append(arr[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                arr.append(nums[i])
                bt(arr, i+1)
                arr.pop()
        
        nums.sort()
        ret = []
        for k in range(len(nums)+1):
            bt([], 0)
        return ret
