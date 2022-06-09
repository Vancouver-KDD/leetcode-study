// 1. using two for loop
var twoSum = function (nums, target) {
  const len = nums.length;
  for (let i = 0; i < len - 1; i++) {
    for (let j = i + 1; j < len; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
};

// 2. using hash table
var twoSum2 = function (nums, target) {
  let table = {};
  for (let i = 0; i < nums.length; i++) {
    let diff = target - nums[i];
    if (table[diff] !== undefined) {
      return [table[diff], i];
    } else {
      table[nums[i]] = i;
    }
  }
};
