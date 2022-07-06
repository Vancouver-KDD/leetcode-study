// Given an array nums containing n distinct numbers in the range [0, n],
// return the only number in the range that is missing from the array.

//* Example 1:

// Input: nums = [3,0,1]
// Output: 2
// Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

//* Example 2:

// Input: nums = [0,1]
// Output: 2
// Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

const missingNumber = function (nums) {
  let xor = 0;
  let i = 0;
  for (i = 0; i < nums.length; i++) {
    xor = xor ^ i ^ nums[i];
  }

  return xor ^ i;
};

// const missingNumber = function (nums) {
//   let sum = 0,
//     total = 0;
//   for (let i = 0; i < nums.length; i++) {
//     sum += nums[i]; // 3 3 4
//     total += i + 1; // 1 3 6
//   }
//   return total - sum; // 6 - 4 = 2
// };

// const missingNumber = function (nums) {
//   let ret = 0;
//   for (let i = 0; i < nums.length; ++i) {
//     ret ^= i;
//     ret ^= nums[i];
//   }
//   return (ret ^= nums.length);
// };
