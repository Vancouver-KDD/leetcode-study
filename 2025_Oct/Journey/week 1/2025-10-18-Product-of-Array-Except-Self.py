class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # variables for pre-computing the prefix and suffix
        prefix = suffix = 1
        answer = [1] * len(nums)

        # multiply each element by the prefix product
        for i in range(len(nums)):
            answer[i] *= prefix
            prefix *= nums[i]

        # multiply each element by the suffix product
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer