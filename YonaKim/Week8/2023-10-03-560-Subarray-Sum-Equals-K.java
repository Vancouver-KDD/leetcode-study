/**
* Time Complexity: O(n^2). n = nums.length. Using nested for loop.
* Space Complexity: O(1). No extra data structure. Constant space used.
*/
class Solution {
    public int subarraySum(int[] nums, int k) {
        int result = 0;

        for(int i = 0; i < nums.length; i++) {
            int sum = 0;
            for(int j = i; j < nums.length; j++) {
                sum += nums[j];
                if(sum == k) {
                    result++;
                }
            }
        }

        return result;
    }
}