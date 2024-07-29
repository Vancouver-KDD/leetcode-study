class Solution:
    def jump(self, nums: List[int]) -> int:
        targetIndex = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= targetIndex:
                targetIndex = i
        return targetIndex == 0
