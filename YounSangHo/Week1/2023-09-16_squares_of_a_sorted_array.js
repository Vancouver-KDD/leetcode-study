/**
 * 배열을 받아 제곱을 하여 그 값을 내림순서로 배열
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function (nums) {
  return nums.map((item) => item * item).sort((a, b) => a - b);
};
