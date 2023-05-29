var missingNumber = function (nums) {
  let map = new Set(nums);

  let expectedLength = nums.length + 1;

  for (let number = 0; number < expectedLength; number++) {
    if (!map.has(number)) {
      return number;
    }
  }

  return -1;
};
