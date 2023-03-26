class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1

        for i in range(target, -1, -1):
            if i + nums[i] >= target:
                target = i

        return True if target == 0 else False