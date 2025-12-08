class Solution {
    /**
        Time Complexity: O(n^2)
        Space Complexity: O(n)
     */
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);

        for (int i = 0; i < nums.length; i++) {
            // finding the max LIS
            for (int j = 0; j < i; j++) {

                // if nums[j] < nums[i], we can extend the LIS
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        int maxLength = 1;
        for (int length : dp) {
            maxLength = Math.max(maxLength, length);
        }

        return maxLength;
    }
}