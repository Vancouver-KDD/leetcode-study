// https://leetcode.com/problems/house-robber-ii/

// similar with previous solution
// 1. breaking the circular arrangement of the houses into two linear arrangements
// use the previous solution function to calculate the maximum amount of money 
// that can be robbed without considering the circular arrangement
public int rob(int[] nums) {
    int n = nums.length;
    if (n == 1) {
        return nums[0];
    }
    int max1 = robHelper(Arrays.copyOfRange(nums, 0, n-1));
    
    int max2 = robHelper(Arrays.copyOfRange(nums, 1, n));
    
    return Math.max(max1, max2);
}

private int robHelper(int[] nums) {
    int n = nums.length;
    if (n == 0) {
        return 0;
    }
    if (n == 1) {
        return nums[0];
    }
    
    int robFirst = nums[0];
    int notRobFirst = 0;
    
    for (int i = 1; i < n; i++) {
        int temp = robFirst;
        robFirst = notRobFirst + nums[i];
        notRobFirst = Math.max(temp, notRobFirst);
    }
    
    return Math.max(robFirst, notRobFirst);
}
