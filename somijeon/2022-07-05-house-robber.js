// You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
//! it will automatically contact the police if two adjacent houses were broken into on the same night.

// Given an integer array nums representing the amount of money of each house,
//todo: return the maximum amount of money you can rob tonight without alerting the police.

//* Example 1:

// Input: nums = [2,7,9,3,1]
// Output: 12
// Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
// Total amount you can rob = 2 + 9 + 1 = 12.

let rob = function (nums) {
  let previous = 0;
  let current = 0;
  let temp;
  for (let x of nums) {
    temp = current;
    current = Math.max(x + previous, current);
    previous = temp;
  }
  return current;
};

// DP solution
// var rob = function (nums) {
//   let dp = [];
//   return findHouses(nums, dp, 0);
// };

// function findHouses(nums, dp, index) {
//   if (index > nums.length - 1) {
//     return 0;
//   }

//   if (dp[index] == undefined) {
//     const skipHouse = findHouses(nums, dp, index + 1);
//     const robHouse = nums[index] + findHouses(nums, dp, index + 2);
//     dp[index] = Math.max(skipHouse, robHouse);
//   }

//   return dp[index];
// }
