## 33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1

₩₩₩
class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) return mid;

            // Left side is sorted
            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;  // target is in the left part
                } else {
                    left = mid + 1;   // target is in the right part
                }
            } 
            // Right side is sorted
            else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;   // target is in the right part
                } else {
                    right = mid - 1;  // target is in the left part
                }
            }
        }

        return -1;
    }
}

₩₩₩

## Time Complexity: O(log n)
Because this solution applies binary search while accounting for the rotation, it still divides the search space by 2 each time.

## Space Complexity: O(1)
No extra memory is used beyond a few variables (left, right, mid). No recursion or data structures.
