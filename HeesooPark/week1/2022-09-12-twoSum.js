// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

// Example 1:

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
// Example 2:

// Input: nums = [3,2,4], target = 6
// Output: [1,2]
// Example 3:

// Input: nums = [3,3], target = 6
// Output: [0,1]


// Constraints:

// 2 <= nums.length <= 104
// -109 <= nums[i] <= 109
// -109 <= target <= 109
// Only one valid answer exists.

var twoSum = (nums, target) => {

    // from the first element, check if the other numbers to be added to become target
    for (let i = 0; i < nums.length; i++) {

        // check from the next num of the array
        for (let j = i+1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) return [i, j]
        }
    }
}

// time complexity O(n^2)

// HashMap { value : index }
// visit first elemnt which is 2, check if (target - 2) exist
// if not, add it to HashMap { 2: 0 } and go to the second element
// find the second : Time O(n) Memo O(n)

var twoSum = function(nums, target) {
    let map = {};

     for (let i = 0; i < nums.length; i++) {
         let diff = target - nums[i]

         // check if it is not undefined, when index 0, it can be falsy value
         if(map[diff] !== undefined) {
             return [map[diff], i]
         }
         map[nums[i]] = i;
     }
};