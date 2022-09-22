


//09-20 현재 이해가 잘 가지 않음 다시 보도록함



const maxProduct = function(nums) {
    // Max product in the current contiguous array
    let currentMax = nums[0];
    // Mind product in the current contiguous array. We need this value in case we encounter
    // 2 negative numbers whose product could potentially give us the max product of the entire array
    let currentMin = nums[0];
    // Max product of a contiguous array
    let finalMax = nums[0];

  for(let i = 1; i < nums.length; i++){
    let temp = currentMax
    // Because we are looking for a contiguous subarray product, the current max must contain the current number in the array.
    currentMax = Math.max(Math.max(currentMax * nums[i], currentMin*nums[i]), nums[i])
    // Use temp here in case the previous currentMax was negative
    currentMin = Math.min(Math.min(temp * nums[i], currentMin*nums[i]), nums[i])
    // Record highest max at the end of every contiguous subarray
    finalMax = Math.max(currentMax, finalMax);
  }

  return finalMax;
};
console.log(maxProduct([2,3,-2,4]))
