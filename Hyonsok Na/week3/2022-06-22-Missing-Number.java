class Solution {
    public int missingNumber(int[] nums) {
        int sum1 = 0;
        for(int i = 1; i<nums.length+1; i++) {
            sum1 += i;
        }
        int sum2 = 0;
        for(int j = 0; j<nums.length; j++) {
            sum2 += nums[j];
        }
        return sum1 - sum2;
    }
}