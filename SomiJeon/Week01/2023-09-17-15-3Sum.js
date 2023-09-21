// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

// Notice that the solution set must not contain duplicate triplets.

//* Example 1:

// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
// Explanation:
// nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
// nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
// nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
//todo: The distinct triplets are [-1,0,1] and [-1,-1,2].
// Notice that the order of the output and the order of the triplets does not matter.

//* Example 2:

// Input: nums = [0,1,1]
// Output: []
// Explanation: The only possible triplet does not sum up to 0.

//* Example 3:

// Input: nums = [0,0,0]
// Output: [[0,0,0]]
// Explanation: The only possible triplet sums up to 0.

var threeSum = function (nums) {
  let n = nums.length;

  nums.sort((a, b) => a - b);

  let result = [];
  for (let i = 0; i < n; i++) {
    if (i > 0 && nums[i - 1] === nums[i]) continue;

    let target = -nums[i];
    for (let L = i + 1, R = n - 1; L < R; ) {
      if (L > i + 1 && nums[L - 1] === nums[L]) {
        L++;
        continue;
      }

      let sum = nums[L] + nums[R];
      if (sum === target) {
        result.push([nums[i], nums[L], nums[R]]);
        L++;
      } else if (sum < target) {
        L++;
      } else {
        R--;
      }
    }
  }
  return result;
};

console.log(threeSum([-1, 0, 1, 0, 0, 0, 0, 1, 1, 1]));
