class Solution:
    def maxProfit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        minNum = nums[0]
        maxProfit = 0
        for num in nums:
            minNum = min(minNum, num)
            maxProfit = max(num - minNum, maxProfit)

        return maxProfit






