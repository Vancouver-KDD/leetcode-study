class Solution:    
    def rob(self, nums: List[int]) -> int:
        def helper(s, e):
            t1, t2 = 0, 0
            for i in range(s, e):
                t1, t2 = max(t1, t2 + nums[i]), t1
            return t1
        if len(nums) == 1:
            return nums[0]

        return max(helper(0, len(nums)-1), helper(1, len(nums)))
        