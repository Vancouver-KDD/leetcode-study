class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums) - 1):
            input1 = nums[i]
            for j in range(i + 1, len(nums)):
                input2 = nums[j]

                if input1 + input2 == target:
                    return [i, j]





nums = [2,7,11,15]
s = Solution()
print(s.twoSum(nums,9))

