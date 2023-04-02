

// Contains Duplicate
// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

// Example 1:
// Input: nums = [1,2,3,1]
// Output: true

// Example 2:
// Input: nums = [1,2,3,4]
// Output: false

// Example 3:
// Input: nums = [1,1,1,3,3,4,3,2,4,2]
// Output: true

// Constraints:
// 1 <= nums.length <= 105
// -109 <= nums[i] <= 109


var containsDuplicate = function(nums) {
    let map = {};

    for(let i=0; i<nums.length; i++) {
        map[nums[i]] = map[nums[i]] ? map[nums[i]] + 1 : 1;
        if(map[nums[i]] >= 2) return true;
    }

    return false;
   
};


// Time Complexity : O(n) Only one traversals are needed, so the time complexity is O(n)
// Space Complexity : O(1) No extra space is needed
