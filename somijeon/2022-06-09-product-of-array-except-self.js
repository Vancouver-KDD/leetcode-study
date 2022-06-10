// Given an integer array nums, return an array result such that result[i] is equal to the product(곱한 값) of all the elements of nums except nums[i].

//todo: You must write an algorithm that runs in O(n) time and without using the division operation.

//* Example 1:

// Input: nums = [1,2,3,4]
// Output: [24,12,8,6] // [1빼고 2*3*4, 1*3*4, ...]

//* Example 2:

// Input: nums = [-1,1,0,-3,3]
// Output: [0,0,9,0,0]

const productExceptSelf = function (nums) {
  var result = [];
  let product = 1;

  for (let i = 0; i < nums.length; i++) {
    result[i] = product;
    product *= nums[i];
  }

  product = 1;

  for (let i = nums.length - 1; i >= 0; i--) {
    result[i] *= product;
    product *= nums[i];
  }

  return result;
};
