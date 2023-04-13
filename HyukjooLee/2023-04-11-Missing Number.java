// Given an array nums containing n distinct numbers in the range [0, n], 
// return the only number in the range that is missing from the array.



// Example 1:

// Input: nums = [3,0,1]
// Output: 2
// Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
// 2 is the missing number in the range since it does not appear in nums.


// Constraints:

// n == nums.length
// 1 <= n <= 104
// 0 <= nums[i] <= n
// All the numbers of nums are unique.


// Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?


// [0,2]
// [0 , 1 , 2]
// [0,1]
// 2 is missing

// 1. using sorting 
// time complexity is O(N logN) due to the sorting step
// space complexity is O(1); constant space to store the result
public int reverseBits(int nums[]) {
    int result = nums.length;

    Arrays.sort(nums);

    for(int i = 0; i < result; i++) {
       if(i !== nums[i]) return i;
    }

    return result;
}

// 2. useing the XOR operation
// Iteration 1: missingNumber = 3 XOR 0 XOR 0 = 3
// Iteration 2: missingNumber = 3 XOR 1 XOR 1 = 3
// Iteration 3: missingNumber = 3 XOR 2 XOR 3 = 2
// time complexity is O(N); the length of array
// space complexity is O(1); constant amount of additional space 
class Solution {
    public int missingNumber(int[] nums) {
            int missingNumber = nums.length;

            for (int i = 0; i < nums.length; i++) {
                missingNumber ^= i ^ nums[i];
            }

            return missingNumber;
    }
}