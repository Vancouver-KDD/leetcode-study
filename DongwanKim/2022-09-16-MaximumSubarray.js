/**
 * Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 */

//first solution
var maxSubArray = function(nums) {
    // max starts with first element of the array
    let max = nums[0];
    let currentMax = 0;
    
    for(let i=0; i<nums.length; i++){
        if(currentMax < 0) currentMax = 0;
        // add current element to currentMax
        currentMax += nums[i];   

        // update max with bigger value
        max = Math.max(max, currentMax)
    }
    
    return max
};

// second solution (kadane's algo)
var maxSubArray = function(nums) {
    // set max with first element of nums
    let max = nums[0];
    // current max is max
    let currentMax = max;
    
    for(let i=1; i<nums.length; i++){

        // compare currentMax + nums[i] and nums[i] then store bigger value
        currentMax = Math.max(currentMax + nums[i], nums[i]);
        // compare currentMax and max then store bigger value
        max = Math.max(currentMax, max);
    }
    
    return max
};