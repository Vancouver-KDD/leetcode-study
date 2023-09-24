// Given an integer array nums sorted in non-decreasing order,
//todo: return an array of the squares of each number sorted in non-decreasing order.

//* Example 1:

// Input: nums = [-4,-1,0,3,10]
// Output: [0,1,9,16,100]
// Explanation: After squaring, the array becomes [16,1,0,9,100].
// After sorting, it becomes [0,1,9,16,100].

//* Example 2:

// Input: nums = [-7,-3,2,3,11]
// Output: [4,9,9,49,121]

var sortedSquares = function (nums) {
  const squaredNums = nums.map((el) => el * el); // TC : O(n), SC : O(n)
  const result = squaredNums.sort((a, b) => a - b); // TC : O(nlogn), SC : O(1)
  // overall TC : O(nlogn), SC : O(n)
  return result;
};

console.log(sortedSquares([-7, 11, 2, 3, -3]));
