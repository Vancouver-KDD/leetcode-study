// Given an integer array nums, return the length of the longest strictly increasing subsequence

// Input: nums = [10,9,2,5,3,7,101,18]
// Output: 4
// Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

// The longest increasing subsequence?
// 주어진 array 에서 어떠한 subarray을 봤을 때, 그 subarray 의 value 들이 오름차순으로 정렬되어 있는 가장 긴 부분수열의 길이

// 1. using DP: again, dp is a solution breaking down a problem into smaller subproblems 
// solve each subproblem only once
// and store the solutions to subproblems in a table to avoid redundant computation
// LIS - 입력 배열의 주어진 인덱스 i에서 끝나는 가장 긴 증가하는 하위 시퀀스의 길이를 찾는것 (하위 문제를 정의)
// 즉, dp[i]는 인덱스 i에서 끝나는 LIS의 길이

// 1. initialize all LIS lengths to 1; dp[i] stores the length of the LIS ending at position i
// 2. iterate through all previous indices j (j < i)
// 3. if the j-th element is less than the i-th element, update the LIS ending at i
// 4. return maxLIS

// time complexity is O(N^2): the length of the input array (a nested loop iterating through all pairs-i,j)
// space complexity O(N): array of size n to store the dp
public static int lengthOfLIS(int[] nums) {
    // 1
    int[] dp = new int[nums.length]; 
    Arrays.fill(dp, 1);

    for (int i = 1; i < nums.length; i++) {
        // 2
        for (int j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                // 3
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
    }
    // 4
    int maxLIS = 0; // stores the length of the longest LIS
    for (int i = 0; i < dp.length; i++) {
        maxLIS = Math.max(maxLIS, dp[i]);
    }

    return maxLIS;
}

// 2. using binary search (better solution)
// tails array will store the smallest tail element
// the length of the LIS found so far
// time complexity O(N logN): Binary search
// space complexity O(N): the length of the input array
public static int lengthOfLIS(int[] nums) {
    int[] tails = new int[nums.length];
    int len = 0; 

    for (int num : nums) {
        int i = 0, j = len;
        while (i < j) {
            int mid = i + (j - i) / 2;
            if (tails[mid] < num) {
                i = mid + 1;
            } else {
                j = mid;
            }
        }
        tails[i] = num;
        if (i == len) {
            len++;
        }
    }

    return len;
}
