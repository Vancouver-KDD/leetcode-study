// Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
//
// Example 1:
//
// Input: nums = [1, 2, 3, 3]
//
// Output: true
// Example 2:
//
// Input: nums = [1, 2, 3, 4]
//
// Output: false

class Solution {
  /**
   * @param {number[]} nums
   * @return {boolean}
   */
  hasDuplicate(nums) {
    if (nums.length === 0) return false;

    const newMap = new Map();
    let result = false;

    nums.forEach((num) => {
      if (newMap.has(num)) {
        result = true;
      } else {
        newMap.set(num, 1);
      }
    });

    return result;
  }
}
