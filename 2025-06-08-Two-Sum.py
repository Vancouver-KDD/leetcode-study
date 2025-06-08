class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in idx:
                return idx[diff], i
            else:
                idx[num] = i
