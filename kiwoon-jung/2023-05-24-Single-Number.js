var singleNumber = function (nums) {
  if (nums.length === 1) {
    return nums[0];
  }

  let result = 0;

  nums.forEach((element) => {
    result = result ^ element;
  });

  return result;
};
