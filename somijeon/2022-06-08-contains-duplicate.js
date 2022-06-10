// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

//* Example 1:

// Input: nums = [1,2,3,1]
// Output: true

//* Example 2:

// Input: nums = [1,2,3,4]
// Output: false

const containsDuplicate = function (nums) {
  const mySet = new Set();
  for (let i = 0; i < nums.length; i++) {
    if (mySet.has(nums[i])) {
      return true;
    }
    mySet.add(nums[i]);
  }
  return false;
};
