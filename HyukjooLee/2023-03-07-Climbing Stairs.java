// You are climbing a staircase. It takes n steps to reach the top.
// Each time you can either climb 1 or 2 steps.
// In how many distinct ways can you climb to the top?

// this problem is about feaguring out how many distinct ways you can reach the top of the staircase
// we can climb one or two steps at a time
// 

// 1. using dynamic programming - break a problem to sub problems
// we can think of climbing stairs as a series of smaller subproblems,
// where we are trying to find the number of ways to climb to each stair position
// by either taking one or two steps
// time complexity is O(N) as 루프를 n번 반복하여 정상에 오르는 고유한 방법을 계산
// space complexity is O(N) as n+1 크기의 배열을 생성
class Solution {
    public int climbStairs(int n) {
    // 첫 번째 단계와 두 번째 단계에 도달하는 방법이 한 가지와 두 가지임을 이미 알고 있음
    if (n == 1) {
        return 1; // one way to climb the stairs
    }

    if(n == 2) {
        return 2; // two way to climb the stairs
    }
    
    // 0-based index 
    // n번째 단계까지 올라가는 방법의 수를 저장
    int[] dp = new int[n + 1];

    // there is only one way to climb to the first step 
    // and two ways to climb to the second step. 
    dp[1] = 1;
    dp[2] = 2;
    
    // we need to consider the previous two stair positions
    // 다음 3에서 n까지의 각 단계 i에 대해 이전 두 단계에 도달하는 방법의 수를 더하여 해당 단계에 도달하는 방법의 수를 계산
    // fill in the rest of the array by adding the number of ways
    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2]; // previous two steps 
    }
    
    return dp[n];
    }
}



// 2. using recursion with memoization
// to store the already computed values 
// time & space - O(N); but space complexity could be more higher as we need an array to store memo

// This function takes an integer n as input and returns the total number of unique ways to climb
// to the top of a staircase with n steps by either taking one step or two steps at a time.
public static int climbStairs(int n) {
    // We initialize an array called memo with a length of n + 1, which will be used to store the
    // results of each subproblem. We then call the helper function with n and memo as arguments.
    int[] memo = new int[n + 1];
    return helper(n, memo);
}

// This function takes an integer n and an array called memo as input and returns the total number
// of unique ways to climb to the top of a staircase with n steps by either taking one step or two
// steps at a time. It uses memoization to avoid redundant computation.
public static int helper(int n, int[] memo) {
    // If n is 1 or 2, there is only one unique way to climb to the top of the staircase.
    if (n == 1 || n == 2) {
        return n;
    }
    // If the result for the subproblem with n steps has already been computed and stored in memo,
    // we simply return that value instead of recomputing it.
    if (memo[n] != 0) {
        return memo[n];
    }
    // Otherwise, we recursively call the helper function with n - 1 and n - 2 as arguments, and
    // add the results together to get the total number of unique ways to climb to the top of the
    // staircase with n steps. We store this value in memo for future reference and return it.
    int res = helper(n - 1, memo) + helper(n - 2, memo);
    memo[n] = res;
    return res;
}
