class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        result = []
        array_size = len(nums)
        for x in range (0, array_size - 1):
            for y in range (x+1, array_size):
                if nums[x] + nums[y] == target:
                    result.append(x)
                    result.append(y)
                    return result
