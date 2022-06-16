// Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

// The test cases are generated so that the answer will fit in a 32-bit integer.

// A subarray is a contiguous subsequence of the array.

//* Example 1:

// Input: nums = [2,3,-2,4]
// Output: 6
// Explanation: [2,3] has the largest product 6.

//* Example 2:

// Input: nums = [-2,0,-1]
// Output: 0
// Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

//Todo: 최대합을 구할 때는 최대값만 있으면 되지만 최대곱을 구할 때는 최소값도 기억하고 있어야 한다.
// 다음 value가 음수이면 절대값이 최대인 최소값을 곱하는 것이 최대값을 창출하기 때문

const maxProduct = function (nums) {
  let currentMax = nums[0];
  let currentMin = nums[0];
  let finalMax = nums[0];

  for (let i = 1; i < nums.length; i++) {
    let temp = currentMax;
    currentMax = Math.max(Math.max(currentMax * nums[i], currentMin * nums[i]), nums[i]);
    currentMin = Math.min(Math.min(temp * nums[i], currentMin * nums[i]), nums[i]);
    finalMax = Math.max(currentMax, finalMax);
  }

  return finalMax;
};

// const maxProduct = function (nums) {
//   let result = Math.max(nums);
//   let curMax = 1;
//   let curMin = 1;
//   for (let el of nums) {
//     if (el === 0) {
//       curMax = 1;
//       curMin = 1;
//       continue;
//     }
//     temp = curMax * el;
//     curMax = Math.max(curMax * el, curMin * el, el); // [-5, 2]의 경우에는 el 자체가 curMax가 되므로 el도 비교한다.
//     curMin = Math.min(temp, curMin * el, el);
//     result = Math.max(result, curMax);
//   }
//   return result;
// };
