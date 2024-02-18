function lengthOfLIS(nums: number[]): number {
  const dp = new Array(nums.length)
  dp.fill(1)
  for (let i = nums.length - 1; i >= 0; --i) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] < nums[j]) {
        dp[i] = Math.max(dp[i], dp[j] + 1)
      }
    }
  }
  return Math.max(...dp)
}
