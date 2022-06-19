// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

// Notice that the solution set must not contain duplicate triplets.

//* Example 1:

// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]

//* Example 2:

// Input: nums = [0]
// Output: []

const threeSum = function (nums) {
  const results = [];
  if (nums.length < 3) return results;
  nums = nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    // i = left
    if (nums[i] > 0) break;

    // i = left, skip numbers we've already seen
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    let j = i + 1; // j = middle
    let k = nums.length - 1; // k = right

    while (j < k) {
      let sum = nums[i] + nums[j] + nums[k];
      if (sum === 0) {
        results.push([nums[i], nums[j], nums[k]]);
        while (nums[j] === nums[j + 1]) j++;
        while (nums[k] === nums[k - 1]) k--;
        j++;
        k--;
      } else if (sum < 0) {
        j++;
      } else {
        k--;
      }
    }
  }

  return results;
};
