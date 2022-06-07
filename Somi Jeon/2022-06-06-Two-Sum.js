const twoSum = function (nums, target) {
  let hashtable = new Map();
  for (let i = 0; i < nums.length; i++) {
    let diff = target - nums[i];

    if (hashtable.hasOwnProperty(diff)) {
      return [hashtable[diff], i];
    }

    hashtable[nums[i]] = i;
  }

  return null;
};
