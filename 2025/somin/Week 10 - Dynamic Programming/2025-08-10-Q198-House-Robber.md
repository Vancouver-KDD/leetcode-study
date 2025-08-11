```
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        if (n == 1) return nums[0];

        int[] dp = new int[n];
        dp[0] = nums[0]; // 첫 번째 집을 털었을 때 최대 금액
        dp[1] = Math.max(nums[0], nums[1]); // 첫 번째와 두 번째 중 더 큰 금액

        for (int i = 2; i < n; i++) {
            // i번째 집을 털 경우 → i-2번째까지의 최대 금액 + 현재 집 돈
            // i번째 집을 털지 않는 경우 → i-1번째까지의 최대 금액
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
        }

        return dp[n - 1]; // 마지막 집까지 고려한 최대 금액
    }
}
```
