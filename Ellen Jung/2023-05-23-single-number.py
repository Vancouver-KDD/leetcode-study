class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        result = []
        for i in nums:
            if i in result:
                result.remove(i)
            else:
                result.append(i)

        return result[0]