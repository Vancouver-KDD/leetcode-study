class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        answer = [1] * len(nums)
    
        prefix = 1
        for i, val in enumerate(nums):
            answer[i] = prefix
            prefix *= val

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
