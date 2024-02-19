https://leetcode.com/problems/maximum-subarray/
class Solution {
    public int maxSubArray(int[] nums) {
        // 1 2 3 4 5 6
        // -1 -2 -3 -4 -5
        // 2 -1 2 3 -2 -3

        int max = Integer.MIN_VALUE;
        int current = 0;
        for(int num : nums) {
            int sum = current + num;
            max = Math.max(max, sum);

            if(sum < 0) {
                current = 0;
            } else {
                current = sum;
            }
        }
        return max;
    }
}