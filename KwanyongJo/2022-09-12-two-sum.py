class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums) - 1):
            value1 = nums[i]
            for j in range(i + 1, len(nums)):
                value2 = nums[j]

                if value1 + value2 == target:
                    return [i, j]


