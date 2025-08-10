class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        temp = [0] * (len(nums) + 1)
        temp[1], temp[2] = nums[0], nums[1]
        for i in range(3, len(nums) + 1):
            temp[i] = max(nums[i - 1] + temp[i - 2], nums[i - 1] + temp[i - 3])
        return max(temp[-2], temp[-1])