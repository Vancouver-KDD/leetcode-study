var twoSum = function (nums, target) {
  const hashTable = new Map();

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    const substractionGoal = target - num;

    if (hashTable.has(substractionGoal)) {
      return [i, hashTable.get(substractionGoal)];
    } else {
      hashTable.set(num, i);
    }
  }
};
