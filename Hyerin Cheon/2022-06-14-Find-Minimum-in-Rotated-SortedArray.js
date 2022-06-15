// 1. O(n)
var findMin = function (nums){
  return Math.min(...nums);
}

// 2. O(log(n))
var findMin = function (nums) {
  let left = 0;
  let right = nums.length - 1;

  if(nums.length === 1) return nums[0];

  while(left < right) {
    let midPoint = Math.floor((left + right) / 2);

    if(nums[right] < nums[midPoint]) {
      left = midPoint + 1;
    } else {
      right = midPoint;
    }
  }
  return nums[left];
}