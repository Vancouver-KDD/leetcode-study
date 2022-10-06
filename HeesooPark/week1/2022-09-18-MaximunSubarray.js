// Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

// A subarray is a contiguous part of an array.



// Example 1:

// Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
// Output: 6
// Explanation: [4,-1,2,1] has the largest sum = 6.
// Example 2:

// Input: nums = [1]
// Output: 1
// Example 3:

// Input: nums = [5,4,-1,7,8]
// Output: 23


// Constraints:

// 1 <= nums.length <= 105
// -104 <= nums[i] <= 104


/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxSubArray = function(nums) {
    // when array doesn't have value ;
    if (nums.length === 0) return 0;

    let max = nums[0];

    for (let i = 0; i < nums.length; i++) {
        let sum = nums[i]
        max = Math.max(max, sum)

        for (let j = i+1; j < nums.length; j++) {
            sum += nums[j]
            max = Math.max(max, sum)
        }
    }
    return max;
}



/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxSubArray = function(nums) {

    // when array doesn't have any value
    if (nums.length === 0) return 0;

    let max = nums[0]
    let sum = 0;

    for ( let n of nums) {
        if (sum < 0) {
            sum = 0
        }
        sum += n

        max = Math.max(sum, max);

    }

    return max;
}