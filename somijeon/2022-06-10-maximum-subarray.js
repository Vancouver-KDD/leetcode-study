// Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

// A subarray is a contiguous part of an array.

//* Example 1:

// Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
// Output: 6
// Explanation: [4,-1,2,1] has the largest sum = 6.

//* Example 2:

// Input: nums = [5,4,-1,7,8]
// Output: 23

const maxSubArray = function (nums) {
  let maxSub = nums[0];
  let curSum = 0;
  for (let el of nums) {
    if (curSum < 0) {
      curSum = 0;
    }
    curSum += el;
    maxSub = Math.max(maxSub, curSum);
  }
  return maxSub;
};

// var maxSubArray = function(nums) {
//   let min = 0;
//   let max = 0;
//   let startIndex = 0;
//   let endIndex = 0;
//   let sum = 0;
//   for (let i = 0; i<nums.length; i++) {
//       sum += nums[i]
//       if(sum >= max) {
//           max = sum
//           endIndex = i
//       }
//       if(sum < min) {
//           min = sum
//           startIndex = i
//       }

//   }
// let result = nums.slice(startIndex, endIndex + 1)
// return result.reduce((a,b) => a+b) 더한 최종 값이 아니라 차이의 절대값 필요
//   return max - min

// };
