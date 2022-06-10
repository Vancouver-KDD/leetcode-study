/*
I: numbers[] - numberes
O: numbers[] - product of all elements except for itself
C: O(n), cannot use division 
*/

var productExceptSelf = function (nums) {
  let leftProduct = [];
  let rightProduct = [];
  let solution = [];

  // leftProduct
  for (let i = 0; i < nums.length; i++) {
    if (leftProduct.length === 0) {
      leftProduct.push(1);
    } else {
      leftProduct.push(leftProduct[i - 1] * nums[i - 1]);
    }
  }

  // rightProduct
  for (let i = nums.length - 1; i >= 0; i--) {
    if (rightProduct.length === 0) {
      rightProduct.push(1);
    } else {
      rightProduct.unshift(rightProduct[0] * nums[i + 1]);
    }
  }

  // solution
  for (let i = 0; i < leftProduct.length; i++) {
    solution.push(leftProduct[i] * rightProduct[i]);
  }

  return solution;
};
