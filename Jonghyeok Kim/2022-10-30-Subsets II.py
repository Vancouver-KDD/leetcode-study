

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(nums, sub):
            res.append(sub)
            if len(nums) == 0:
                return
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i-1]:
                    dfs(nums[i+1:], sub+[nums[i]])
        dfs(nums, [])
        return res