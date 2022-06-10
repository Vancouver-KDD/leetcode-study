function maxSubArray(nums) {
  // if theres only one number in array then just return that number
  if(nums.length === 1) return nums[0];

  let maxValue = nums[0];
  let accNum = nums[0];

  //
  for(let i = 1; i < nums.length; i++){
    // check if the current number is big or should I take my previous accumulated number
    let calc = Math.max(nums[i], accNum + nums[i]);

    if(calc > maxValue) maxValue = calc;
    accNum = calc;
  }
  return maxValue;

  // TC: O(n)
  // SC: O(1)
};