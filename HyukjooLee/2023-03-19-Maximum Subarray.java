// Given an integer array nums, find the subarray with the largest sum, and return its sum.

// Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
// Output: 6
// Explanation: The subarray [4,-1,2,1] has the largest sum 6.

// int array 에서 합이 가장 큰 subarray 를 찾고 그 합을 return 하는 문제
// using Kadane algorithmm; useful for solving the maximum subarray problems
// 1. 두 변수 maxSumEndingHere / maxSumSoFar
// 2. loop the nums array starting from the second element
// 3. update maxSumEndingHere to be the maximum of the current element 
// and the sum of the current element and maxSumEndingHere.

// current position 에서 어떻게 업데이트 되는가?
// Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
// i = 0: maxSumEndingHere = -2, maxSoFar = -2
// i = 1: maxSumEndingHere = 1, maxSoFar = 1
// i = 2: maxSumEndingHere = -2, maxSoFar = 1
// i = 3: maxSumEndingHere = 4, maxSoFar = 4
// i = 4: maxSumEndingHere = 3, maxSoFar = 4
// i = 5: maxSumEndingHere = 5, maxSoFar = 5
// i = 6: maxSumEndingHere = 6, maxSoFar = 6
// i = 7: maxSumEndingHere = 1, maxSoFar = 6
// i = 8: maxSumEndingHere = 5, maxSoFar = 6

// 4. update maxSoFar to be the maximum of maxSoFar and maxSumEndingHere.
// 5. return maxSoFar

// The time complexity of Kadane's algorithm is O(N): the length of the input array
// The space complexity is O(1): it uses only two variables to store those two vars
public static int maxSubArray(int[] nums) {
    // 1
    int maxSumSoFar = nums[0];
    int maxSumEndingHere = nums[0]; 

    // 2
    for (int i = 1; i < nums.length; i++) {
        // 3
        maxSumEndingHere = Math.max(nums[i], maxSumEndingHere + nums[i]);
        // 4
        maxSumSoFar = Math.max(maxSumSoFar, maxSumEndingHere);
    }
    // 5
    return maxSumSoFar;
}