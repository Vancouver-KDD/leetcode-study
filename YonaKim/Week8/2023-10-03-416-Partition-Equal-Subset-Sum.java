/**
* Time Complexity: O(m*n). n is nums.length, and m is sum (sum of subset)
* Space Complexity: O(m). We use an extra boolean array of size m
*/
class Solution {
    public boolean canPartition(int[] nums) {
        if(nums.length == 0) {
            return false;
        }

        int totalSum = 0;
        for(int n : nums) {
            totalSum += n;
        }

        //if total sum is odd, cannot partition into two equal subsets
        if(totalSum%2 == 1) {
            return false;
        }

        int sum = totalSum / 2;

        boolean dp[] = new boolean[sum + 1];
        dp[0] = true;

        for(int n: nums) {
            for(int i = sum; i >= n; i--) {
                dp[i] |= dp[i - n];
            }
        }

        return dp[sum]; 
    }
}