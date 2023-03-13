// You are climbing a staircase. It takes n steps to reach the top.
// Each time you can either climb 1 or 2 steps.
// In how many distinct ways can you climb to the top?

// 5 => 8
// 1,1,1,1,1
// 1,2,2
// 2,1,2
// 2,2,1
// 2,1,1,1
// 1,2,1,1
// 1,1,2,1
// 1,1,1,2

// 1,2,3,5,8

// using dynamic programming - break a problem to sub problems
// fibonacci sequence
// time complexity is O(N)
// space complexity is O(N) as we need to store an array of size n+1 to store the intermediate results
class Solution {
    public int climbStairs(int n) {
    if (n == 1) {
        return 1;
    }

    if(n == 2) {
        return 2;
    }
    
    int[] dp = new int[n + 1];
    dp[1] = 1;
    dp[2] = 2;
    
    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    
    return dp[n];
    }
}
