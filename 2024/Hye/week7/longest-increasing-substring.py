""" 300. Longest Increasing Subsequence / Medium

Given an integer array nums, return the length of the longest strictly increasing 
subsequence


Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 
Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        1. Iterate through the nums and append increasing numbers in results
        2. If the num is not in increasing order, replace it with one of the
           numbers in the results that is the next bigger number
        Example:
        # Input: nums = [10,9,2,5,3,7,101,18]
        results.append(10)
        [10]
        results. replace 10 with 9, as results[-1] > num 
        [9]
        replace 9 with 2, as results[-1] > num 
        This is okay because it doesn't increase the length of the results array
                 (== increasing subsequence number list)
        [2]
        results.append(5)
        [2, 5]
        results.replace 5 with 3 - use binary search to find which number to swap
        [2, 3]
        """

        def binary_search(num, results):
            left, right = 0, len(results) - 1
            while left <= right:
                mid = (left + right) // 2
                if results[mid] == num:
                    return mid
                elif results[mid] > num:
                    right = mid - 1
                else:
                    left = mid + 1

            return left

        results = []
        for num in nums:
            if not results or results[-1] < num:
                results.append(num)
            else:
                # Find index to swap with the current num
                # num < result[index] (smallest larger numbers)
                index = binary_search(num, results)
                results[index] = num

        return len(results)

        # Time complexity: O(nlogn) - binary search for each number
        # Space complexity: O(n) - results
