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

let maxSubArray = function (nums) {


  let maxSum = nums[0];

  for (let a = 1; a < nums.length; a++) {
    nums[a] = Math.max(nums[a], nums[a] + nums[a - 1])
    maxSum = Math.max(nums[a], maxSum)
  }
  return maxSum
};

console.log(maxSubArray([-2, -1]))
