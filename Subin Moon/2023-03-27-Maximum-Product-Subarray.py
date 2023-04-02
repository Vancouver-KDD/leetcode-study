"""
Given an integer array nums, find a subarray that has the largest product, and return the product.
* A subarray is a contiguous non-empty sequence of elements within an array.

The test cases are generated so that the answer will fit in a 32-bit integer.

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
class Solution:
    # O(n); memory -> O(1)
    def maxProduct(self, nums: list[int]) -> int:
        # If all positive nums -> product increasing
        # If all negative nums -> keep both max and min because the product of two subarrays, there are two different outcomes depending on whether the next element is a negative number or not
        # If there is a 0 -> keep the max and min as 1

        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)  # [-1, 8]
            curMin = min(tmp, n * curMin, n)  # [-1, -8]
            res = max(res, curMax)
        return res

    def maxProduct_2(self, nums):
        reverse = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reverse[i] *= nums[i - 1] or 1
        return max(nums + reverse)
