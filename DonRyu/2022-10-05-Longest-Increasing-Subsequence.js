var lengthOfLIS = function (nums) {
    // Create dp array
    const dp = Array.from(nums, () => 1);
    // Max subsequence length
    let max = 1
    // Check all increasing subsequences up to the current ith number in nums
    for (let i = 1; i < nums.length; i++) {
        // Keep track of subsequence length in the dp array
        for (let j = 0; j < i; j++) {
            // Only change dp value if the numbers are increasing
            if (nums[i] > nums[j]) {
                // Set the value to be the larget subsequence length
                dp[i] = Math.max(dp[i], dp[j] + 1)
                // Check if this subsequence is the largest
                max = Math.max(dp[i], max)
            }
        }
    }
  return max;
};
