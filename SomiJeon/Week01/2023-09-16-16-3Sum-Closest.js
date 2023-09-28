// Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

//todo:  Return the sum of the three integers.

// You may assume that each input would have exactly one solution.

//* Example 1:

// Input: nums = [-1,2,1,-4], target = 1
// Output: 2
// Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

//* Example 2:

// Input: nums = [0,0,0], target = 1
// Output: 0
// Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

var threeSumClosest = function (nums, target) {
  const sortedArray = nums.sort((a, b) => a - b);
  let minAbsDiff = Infinity;
  let closestSum = 0;
  for (let i = 0; i < sortedArray.length - 2; i++) {
    let left = i + 1;
    let right = sortedArray.length - 1;
    while (left < right) {
      const currentSum = sortedArray[i] + sortedArray[left] + sortedArray[right];
      const currentDiff = Math.abs(currentSum - target);
      if (currentDiff === 0) {
        return target;
      } else if (currentDiff < minAbsDiff) {
        minAbsDiff = currentDiff;
        closestSum = currentSum;
      } else if (currentSum < target) {
        left++;
      } else {
        right--;
      }
    }
  }
  return closestSum;
};

// The overall time complexity (TC) of the provided code is approximately O(n*log(n)) for sorting the array and O(n^2) for the nested loops, resulting in an overall TC of O(n^2) since the nested loops dominate the time complexity.
