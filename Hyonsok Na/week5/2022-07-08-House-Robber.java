class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1)
            return nums[0];
        else if (nums.length == 2)
            return Math.max(nums[0], nums[1]);
        
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);
        
        for (int i = 2; i < nums.length; i++) {
            if(nums[i] + dp[i-2] > dp[i-1]) {
                dp[i] = nums[i] + dp[i-2];
            } else {
                dp[i] = dp[i-1];
            }
        }
        

        return dp[dp.length - 1];
    }
}