class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length_nums = len(nums)
        output = [1] * length_nums
        prefix = 1
        postfix = 1
        for i in range(length_nums):
            output[i] = prefix
            prefix *= nums[i]

        for i in range(length_nums-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output

# nums = [1,2,3,4]
# s = Solution()
# print(s.productExceptSelf(nums))