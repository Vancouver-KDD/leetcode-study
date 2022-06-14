function maxProduct(nums) {
  
  // [ -2, 4, -2, 4]
  //          4 -8  -8 16  64 -32
  // max = -2,  4,   16,    64
  // min = -2, -8,   -8,   -32
  // finalMax = -2, 4. 16, 64

  let min = nums[0];
  let max = nums[0];
  let finalMax = nums[0];

  for(let i = 1; i < nums.length; i++){
    let tempMax = max;
    max = Math.max(nums[0] * max, nums[0] * min, nums[i]);
    min = Math.min(nums[0] * tempMax, nums[0] * min, nums[i]);

    if(max > finalMax) finalMax = max;
  }
  return finalMax;
};