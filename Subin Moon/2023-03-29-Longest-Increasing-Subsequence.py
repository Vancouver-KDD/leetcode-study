"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

* A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Input: nums = [0,1,0,3,2,3]
Output: 4

Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
class Solution:
    # Brute Force - DFS: Find every single subsequence. Every element has two choices either include the next element or not -> O(2^n)
    # Cached
    def lengthOfLIS(self, nums: list[int]) -> int:
        # 1. Decide from which element to start
        # 2. On each element: decide from where to start again
        # 3. Expand the decision tree until we get unincreasing subsequence
        # 4. Think from the end. If we start at the latter index and store it to somewhere, this will be repeated on the earlier index

        # DP (e.g. [1, 2, 4, 3] O(n^2)
        # The last index is 1, the base case  lis[3] = 1
        # only if nums[2] < nums[3]: lis[2] = max(1, 1 + lis[3]) = 1, in this case lis[2] = 1
        # lis[1] = max(1, 1+lis[2], 1+lis[3]) = 2
        # lis[0] = max(1, 1+lis[1], 1+lis[2], 1+lis[3]) = 3
        lis = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1): # Start from the end
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])
        return max(lis)

    def lengthOfLIS_op(self, nums):  # O(n logn)
        def binarySearch(sub, val):
            lo, hi = 0, len(sub) - 1
            while (lo <= hi):
                mid = lo + (hi - lo) // 2
                if sub[mid] < val:
                    lo = mid + 1
                elif val < sub[mid]:
                    hi = mid - 1
                else:
                    return mid
            return lo

        sub = []
        for val in nums:
            pos = binarySearch(sub, val)
            if pos == len(sub):
                sub.append(val)
            else:
                sub[pos] = val
        return len(sub)
