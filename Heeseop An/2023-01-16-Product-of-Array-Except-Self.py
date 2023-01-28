class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fromL = [1] * len(nums)
        fromR = [1] * len(nums)
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            prefix *= nums[i]
            fromL[i] = prefix

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix *= nums[i]
            fromR[i] *= suffix

        print(fromR)

        for i in range(len(nums)):
            if i == 0:
                result[i] = fromR[i + 1]
            elif i == len(nums) - 1:
                result[i] = fromL[i - 1]
            else:
                result[i] = fromR[i + 1] * fromL[i - 1]

        return result