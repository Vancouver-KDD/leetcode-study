"""
152. Maximum Product Subarray / Medium

Given an integer array nums, find a subarray that has the largest product, 
and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 
Constraints:
1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        the negative number will swap the max_num and min_num
        keep track of min and max as you add the products
        """

        max_num = 1
        min_num = 1
        result = 0
        for num in nums:
            temp_max_num = max_num * num
            max_num = max(max_num * num, min_num * num, num)  # the last part is for 0 edge case?
            min_num = min(temp_max_num, min_num * num, num)
            result = max(result, max_num)
        return result
