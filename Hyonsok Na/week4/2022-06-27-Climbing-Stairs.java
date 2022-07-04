class Solution {
    public int climbStairs(int n) {
        int sum1 = 1;
        int sum2 = 0;
        int sum3 = 0;
        for(int i = 0; i<n+1; i++) {
            sum3 = sum1 + sum2;
            sum1 = sum2;
            sum2 = sum3;
        }
        return sum3;
    }
}