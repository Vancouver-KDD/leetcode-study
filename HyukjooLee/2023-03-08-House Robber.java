// You are a professional robber planning to rob houses along a street.
// Each house has a certain amount of money stashed, the only constraint stopping you 
// from robbing each of them is that adjacent houses have security systems connected 
// and it will automatically contact the police if two adjacent houses were broken into on the same night.

// Given an integer array nums representing the amount of money of each house,
// return the maximum amount of money you can rob tonight without alerting the police.

// Input: nums = [1,2,3,1]
// Output: 4
// Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
// Total amount you can rob = 1 + 3 = 4.

// 1. using dynamic programming to keep track of the maximum amount of money 
// that can be robbed with or without robbing each house
// start by creating two variables
// 1) the maximum amount of money that can be robbed with the current house
// 2) the maximum amount of money that can be robbed without the current house
// then, we loop through the remaining houses, updating these variables
// time complexity of this solution is O(N)
// space complexity is O(1)
public int rob(int[] nums) {
    int n = nums.length;
    if (n == 0) {
        return 0;
    }
    if (n == 1) {
        return nums[0];
    }
    
    // create two variables to store the maximum amount of money that can be robbed
    // with or without robbing the first house, respectively.
    int robFirst = nums[0];
    int notRobFirst = 0;
    
    // loop through the remaining houses, updating the maximum amount of money
    // that can be robbed with or without robbing the current house.
    for (int i = 1; i < n; i++) {
        int temp = robFirst;
        robFirst = notRobFirst + nums[i];
        notRobFirst = Math.max(temp, notRobFirst);
    }
    
    // return the maximum of the two variables.
    return Math.max(robFirst, notRobFirst);
}
