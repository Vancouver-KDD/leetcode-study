class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curMax = 0

        for n in nums:
            if (curMax < 0):
                curMax = 0
            curMax += n
            maxSub = max(maxSub, curMax)
        return maxSub