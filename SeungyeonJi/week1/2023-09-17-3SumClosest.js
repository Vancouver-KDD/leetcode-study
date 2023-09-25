let ThressSumClosest = function (nums, target) {
  nums.sort((a, b) => a - b);
  let n = nums.length;
  let closestSum = nums[0] + nums[1] + nums[2];
  for (let i = 0; i < n - 2; i++) {
    let start = i + 1;
    let end = n - 1;
    while (start < end) {
      let sum = nums[i] + nums[start] + nums[end];
      if (sum === target) {
        return sum;
      } else if (sum < target) {
        start++;
      } else {
        end--;
      }

      if (Math.abs(sum - target) < Math.abs(closestSum - target)) {
        closestSum = sum;
      }
    }
  }
  return closestSum;
};
