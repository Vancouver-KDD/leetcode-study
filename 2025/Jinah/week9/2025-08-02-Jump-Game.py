from ast import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastIdx = len(nums)-1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= lastIdx:
                lastIdx = i

        return True if lastIdx == 0 else False