var containsDuplicate = function (nums) {
  // 1. Create a new numSet.
  const numSet = new Set();

  // 2. Loop through nums
  for (let i = 0; i < nums.length; i++) {
    // a. If numSet has current num return true.
    if (numSet.has(nums[i])) {
      return true;
    } // b. Add current num to numSet
    numSet.add(nums[i]);
  }
  // 3. Return false
  return false;
};
