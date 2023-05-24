class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in range(0, len(nums) + 1):
            if x not in nums:
                return x