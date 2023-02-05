# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

class Solution:
    # Solution 1 - Space-Optimized Prefix & Suffix Products in One-pass
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1 for _ in range(len(nums))]
        pre = 1
        post = 1

        for i in range(len(nums)):
            result[i] *= pre
            pre = pre * nums[i]
            result[- i - 1] *= post
            post = post * nums[- i - 1]

        return result

    # Solution 2 - Space-Optimized Prefix & Suffix Products
    def productExceptSelf_sol2(self, nums: list[int]) -> list[int]:
        length = len(nums)
        result = [1 for _ in range(length)]
        suff_prod = 1

        for i in range(1, length):
            result[i] = result[i-1] * nums[i-1]
        for i in range(length-1, -1, -1):
            result[i] *= suff_prod
            suff_prod *= nums[i]

        return result