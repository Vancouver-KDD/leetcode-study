"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""
import sys


class Solution:
    # Solution 1: Binary Search
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1
        res = sys.maxsize

        # When the last element is greater than the first element = not rotated
        if nums[right] > nums[left]:
            return nums[left]

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                right -= 1
            else:
                res = min(res, nums[right])
                left += 1

        return res

    # Solution 2: Optimized Binary Search
    def findMin_2(self, nums):
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1

        if nums[right] > nums[0]:
            return nums[0]

        while right >= left:
            mid = left + (right - left) // 2
            # If mid > mid+1, mid+1 is the smallest
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if mid < mid-1, mid is the smallest
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            # If mid > nums[0], the least value is still somewhere to the right
            if nums[mid] > nums[0]:
                left = mid + 1
            # If mid < nums[0], the smallest value is somewhere to the left
            else:
                right = mid - 1
