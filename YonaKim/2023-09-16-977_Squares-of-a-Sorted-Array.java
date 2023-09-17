/**
Time Complexity: O(N), where N is the length of array.

Space Complexity: O(N) if you take output into account and O(1) otherwise.
 */
class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int left = 0;
        int right = n-1;
        
        int square = 0;
        int[] result = new int[n];
        for(int i = n-1; i >= 0; i--) {
            if(Math.abs(nums[left]) > Math.abs(nums[right])) {
                square = nums[left];
                left ++;
            } else {
                square = nums[right];
                right --;
            }
            result[i] = (int)Math.pow(square,2);
        }

        return result;
    }
}
