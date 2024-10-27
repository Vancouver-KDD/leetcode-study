"""Find Target in Rotated Sorted Array
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:
Input: nums = [3,4,5,6,1,2], target = 1
Output: 4

Example 2:
Input: nums = [3,5,6,0,1,2], target = 4
Output: -1

Constraints:
1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-1000 <= target <= 1000
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        target= 2
        [4, 5, 7, 8, 1, 2, 3]

        nums=[3,5,1]
        target=3

        When checking the mid point, if left < right, it not, you're still in the rotated array
        in rotated array:
            if nums[mid] > target:
                go to opposite direction
                right = mid + 1
            else:
                left = mid - 1
        
        """
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                # ascending order on the left side
                if nums[mid] < target or nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1

            else:
                # rotated
                # target 1, nums[mid] = 2
                # Ex) [6, 8, 1, 2, 3, 5]
                # and case target 8 is covered by nums[right] < target
                if nums[mid] > target or nums[right] < target:
                    right = mid - 1
                else:
                    left = mid + 1
    
        return -1
