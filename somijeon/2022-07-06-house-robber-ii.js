// You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
//! All houses at this place are arranged in a circle.
// That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

// Given an integer array nums representing the amount of money of each house,
//todo: return the maximum amount of money you can rob tonight without alerting the police.

// Example 1:

// Input: nums = [2,3,2]
// Output: 3
// Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

// Example 2:

// Input: nums = [1,2,3,1]
// Output: 4
// Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
// Total amount you can rob = 1 + 3 = 4.

var rob = function (nums) {
  let n = nums.length;
  if (n == 1) return nums[0];

  return Math.max(robHouses(1, n - 1), robHouses(0, n - 2));

  function robHouses(start, end) {
    const len = end - start + 1;
    const dp = [];
    (dp[0] = 0), (dp[1] = 0); // For look-backs

    for (let i = 0, j = 2; i < len; i++, j++) {
      const num = nums[start + i];
      dp[j] = Math.max(num + dp[j - 2], dp[j - 1]);
    }

    return dp[dp.length - 1];
  }
};
