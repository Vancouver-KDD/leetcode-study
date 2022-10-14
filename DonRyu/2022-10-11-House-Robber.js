var rob = function(nums) {
    if (nums.length === 0) return 0;
    if (nums.length === 1) return nums[0]

    // Keep track of the max money we can make with x amount of houses available
    // dp[0] = max amount if we only have the first house to rob
    // dp[1] = max amount if we only have the first 2 houses to rob
    let dp = [nums[0], Math.max(nums[0], nums[1])];

    for (let i = 2; i < nums.length; i++) {
        // Compare current max with the previous max
        // Check if the money from the current house + max of 2 houses away is greater than the current max
        dp[i] = Math.max(dp[i-2] + nums[i], dp[i-1]);
    }
    return dp[nums.length - 1];
};
