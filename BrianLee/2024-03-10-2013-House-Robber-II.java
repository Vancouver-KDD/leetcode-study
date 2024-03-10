https://leetcode.com/problems/house-robber-ii/

class Solution {
    public int rob(int[] nums) {
        if(nums.length == 1) return nums[0];
        return Math.max(calculate(nums, 1, nums.length), calculate(nums, 0, nums.length-1));
    }

    private int calculate(int[] nums, int start, int length) {
        int sum1 = 0;
        int sum2 = 0;

        for(int i = start; i < length; i++) {
            int newSum = Math.max(sum1+nums[i], sum2);
            sum1 = sum2;
            sum2 = newSum;
        }
        return sum2;
    }
}