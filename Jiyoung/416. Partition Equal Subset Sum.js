var canPartition = function(nums) {
    const total = nums.reduce((cur, acc) => cur + acc, 0);
    if (total % 2 === 1) return false;

    const half = total / 2;
    var dp = [];
    dp[0] = true;
    for (var index = 0; index < nums.length; index++) {
        var num = nums[index];
        for (var i = half; i >= num; i--) {
            dp[i] = dp[i] || dp[i - num];
        }
    }
    return dp[half] || false;
};
