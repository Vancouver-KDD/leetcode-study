class Solution {
    public int lengthOfLIS(int[] nums) {
        int len = nums.length;
        int [] dp = new int[len];
        int max = 1;

        for(int i = 0; i<len;i++) {
            dp[i] = 1;
            for(int j = 0; j<i;j++) {
                if(nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j]+1);
                    max = Math.max(dp[i], max);
                }
            }
        }
        return max;
    }
    //Word break과 같은 방법이다.
    //TC : O(N^2)

    //For better TC
    //binary search로?
    public int lengthOfLIS2(int[] nums) {
        int[] tails = new int[nums.length];
        int size = 0;
        for (int x : nums) {
            int i = 0, j = size;
            while (i != j) {
                int m = (i + j) / 2;
                if (tails[m] < x)
                    i = m + 1;
                else
                    j = m;
            }
            tails[i] = x;
            if (i == size) ++size;
        }
        return size;
    }
}