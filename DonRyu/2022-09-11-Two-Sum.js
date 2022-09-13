const twoSum = function (nums, target) {

  for (let a = 0; a < nums.length; a++) {

    let index0 = a;

    for (let b = 0; b < nums.length; b++) {

      let index1 = b;

      if (a !== b && nums[a] + nums[b] === target) {
        return [index0, index1]
      }
    }
  }
};

console.log(twoSum([3, 3], 6))
