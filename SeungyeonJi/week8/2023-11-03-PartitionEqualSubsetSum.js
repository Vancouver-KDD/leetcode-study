var canPartition = function (nums) {
  var sum = nums.reduce((a, b) => a + b, 0);

  if (sum % 2 !== 0) {
    return false;
  }

  var half = sum / 2;

  var dp = [];

  dp[0] = true;

  for (var index = 0; index < nums.length; ++index) {
    var num = nums[index];
    for (var i = half; i >= num; --i) {
      dp[i] = dp[i] || dp[i - num];
    }
  }

  return dp[half] || false;
};
