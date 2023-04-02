class Solution:
    def rob(self, nums: List[int]) -> int:
        def robrob(nums):
            rob, not_rob = 0, 0
            for num in nums:
                rob, not_rob = not_rob + num, max(rob, not_rob)
            return max(rob, not_rob)

        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(robrob(nums[1:]), robrob(nums[:-1]))